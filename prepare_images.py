from __future__ import annotations

import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
MAX_BYTES = 30 * 1024 * 1024
USER_AGENT = "daily-yidian/3.0 (+https://aa-lin-bot.github.io/daily-yidian/)"


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing YAML front matter: {path}")
    _, header, _ = text.split("---\n", 2)
    return yaml.safe_load(header) or {}


def safe_target(path_text: str) -> Path:
    rel = Path(path_text)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError(f"Unsafe image path: {path_text}")
    if len(rel.parts) < 2 or rel.parts[0] != "assets" or rel.parts[1] != "images":
        raise ValueError(f"Images must be stored under assets/images/: {path_text}")
    return ROOT / rel


def download(url: str, target: Path) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError(f"Unsupported image URL: {url}")

    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".part")

    last_error = None
    for attempt in range(1, 6):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                },
            )
            with urllib.request.urlopen(req, timeout=45) as response:
                content_type = response.headers.get_content_type()
                total = 0
                with tmp.open("wb") as fh:
                    while True:
                        chunk = response.read(1024 * 256)
                        if not chunk:
                            break
                        total += len(chunk)
                        if total > MAX_BYTES:
                            raise ValueError(f"Image exceeds {MAX_BYTES} bytes: {url}")
                        fh.write(chunk)

                if total < 256:
                    raise ValueError(f"Downloaded file is unexpectedly small: {url}")
                if not (content_type.startswith("image/") or target.suffix.lower() == ".svg"):
                    raise ValueError(f"Unexpected Content-Type {content_type}: {url}")

            os.replace(tmp, target)
            print(f"Downloaded {url} -> {target.relative_to(ROOT)}")
            return
        except urllib.error.HTTPError as exc:
            last_error = exc
            if tmp.exists():
                tmp.unlink()
            if attempt < 5:
                retry_after = exc.headers.get("Retry-After")
                if exc.code == 429:
                    if retry_after and retry_after.isdigit():
                        delay = max(5, int(retry_after))
                    else:
                        delay = min(30, attempt * 5)
                else:
                    delay = min(10, attempt * 2)
                print(f"Download attempt {attempt} failed ({exc.code}); retrying in {delay}s: {url}")
                time.sleep(delay)
        except Exception as exc:
            last_error = exc
            if tmp.exists():
                tmp.unlink()
            if attempt < 5:
                delay = min(10, attempt * 2)
                print(f"Download attempt {attempt} failed; retrying in {delay}s: {url}")
                time.sleep(delay)

    raise RuntimeError(f"Failed to download {url}: {last_error}")


def main() -> None:
    images = {}
    for article_path in sorted(CONTENT.glob("**/article-*.md")):
        meta = read_frontmatter(article_path)
        for image in meta.get("images", []):
            path_text = image.get("path")
            url = image.get("download_url")
            if not path_text or not url:
                raise ValueError(
                    f"{article_path}: every image requires path and download_url"
                )
            previous = images.get(path_text)
            if previous and previous != url:
                raise ValueError(
                    f"Conflicting download URLs for {path_text}: {previous} vs {url}"
                )
            images[path_text] = url

    if not images:
        raise ValueError("No images found in published content")

    for path_text, url in images.items():
        target = safe_target(path_text)
        if target.exists() and target.stat().st_size >= 256:
            print(f"Using existing {target.relative_to(ROOT)}")
            continue
        download(url, target)
        time.sleep(1.5)

    print(f"Prepared {len(images)} published image assets")


if __name__ == "__main__":
    main()
