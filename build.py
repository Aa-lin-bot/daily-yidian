from __future__ import annotations

import base64
import hashlib
import json
import mimetypes
import re
import shutil
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from email.utils import format_datetime
from html import escape
from pathlib import Path

import jinja2
import mistune
import yaml

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
ASSETS = ROOT / "assets"

CONFIG = yaml.safe_load((ROOT / "config" / "site.yml").read_text(encoding="utf-8"))
SITE_URL = CONFIG["site_url"].rstrip("/") + "/"
SITE_NAME = CONFIG["name"]
TZ = timezone(timedelta(hours=int(CONFIG.get("utc_offset_hours", 8))))

md = mistune.create_markdown(escape=False)
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES),
    autoescape=jinja2.select_autoescape(["html", "xml"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


def read_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing YAML front matter: {path}")
    _, header, body = text.split("---\n", 2)
    return yaml.safe_load(header) or {}, body.strip()


def ensure_clean_site() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    shutil.copytree(STATIC, SITE / "static")
    if ASSETS.exists():
        shutil.copytree(ASSETS, SITE / "assets")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")


def render_to(template_name: str, out: Path, **ctx) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(env.get_template(template_name).render(**ctx), encoding="utf-8")


def slugify(value: str) -> str:
    ascii_slug = re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")
    return ascii_slug or hashlib.sha1(value.encode("utf-8")).hexdigest()[:10]


def image_html(article: dict, index: int, root: str) -> str:
    images = article.get("images", [])
    if index >= len(images):
        return ""
    img = images[index]
    src = root + img["path"]
    caption = escape(img.get("caption", ""))
    credit = escape(img.get("credit", ""))
    license_text = escape(img.get("license", ""))
    detail = " · ".join(x for x in [credit, license_text] if x)
    caption_html = f"{caption}{' · ' if caption and detail else ''}{detail}"
    return (
        f'<div class="inline-img"><img class="zoomable" loading="lazy" src="{src}" '
        f'alt="{escape(img.get("alt", ""))}">'
        f'<div class="caption">{caption_html}</div></div>'
    )


def article_body_html(article: dict, root: str) -> str:
    body = article["body_markdown"]
    body = re.sub(
        r"\[\[image:(\d+)\]\]",
        lambda m: image_html(article, int(m.group(1)), root),
        body,
    )
    return md(body)


def data_uri(path_str: str) -> str:
    path = ROOT / path_str
    data = path.read_bytes()
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"


def offline_body_html(article: dict) -> str:
    body = article["body_markdown"]

    def repl(match):
        idx = int(match.group(1))
        img = article["images"][idx]
        src = data_uri(img["path"])
        caption = escape(img.get("caption", ""))
        credit = escape(img.get("credit", ""))
        license_text = escape(img.get("license", ""))
        detail = " · ".join(x for x in [credit, license_text] if x)
        caption_html = f"{caption}{' · ' if caption and detail else ''}{detail}"
        return (
            f'<div class="inline-img"><img src="{src}" alt="{escape(img.get("alt", ""))}">'
            f'<div class="caption">{caption_html}</div></div>'
        )

    body = re.sub(r"\[\[image:(\d+)\]\]", repl, body)
    return md(body)


def load_content() -> tuple[list[dict], list[dict]]:
    articles = []
    for path in sorted(CONTENT.glob("**/article-*.md")):
        meta, body = read_frontmatter(path)
        meta["body_markdown"] = body
        meta["source_path"] = path.as_posix()
        meta["url"] = f"articles/{meta['slug']}/"
        articles.append(meta)

    by_slug = {a["slug"]: a for a in articles}
    issues = []
    for path in sorted(CONTENT.glob("**/issue.yml")):
        issue = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        issue_articles = []
        for slug in issue.get("articles", []):
            if slug not in by_slug:
                raise ValueError(f"Issue references unknown article slug: {slug}")
            issue_articles.append(by_slug[slug])
        issue["article_objects"] = issue_articles
        issue["url"] = f"issues/{int(issue['issue']):03d}/"
        issues.append(issue)

    issues.sort(key=lambda x: x["date"])
    return articles, issues


def validate(articles: list[dict], issues: list[dict]) -> None:
    required = [
        "id", "title", "slug", "date", "category", "tags", "summary",
        "difficulty", "reading_minutes", "images", "sources",
    ]
    seen_ids, seen_slugs = set(), set()

    for article in articles:
        missing = [k for k in required if k not in article]
        if missing:
            raise ValueError(f"{article.get('source_path')} missing: {missing}")
        if article["id"] in seen_ids or article["slug"] in seen_slugs:
            raise ValueError(f"Duplicate article id/slug: {article['id']} / {article['slug']}")
        seen_ids.add(article["id"])
        seen_slugs.add(article["slug"])
        images = article.get("images", [])
        if not images:
            raise ValueError(f"{article['source_path']}: at least one image is required")
        for img in images:
            image_required = ["path", "download_url", "original_url", "alt", "caption", "credit", "license"]
            image_missing = [k for k in image_required if not img.get(k)]
            if image_missing:
                raise ValueError(f"{article['source_path']}: image metadata missing {image_missing}")
            if not (ROOT / img["path"]).exists():
                raise FileNotFoundError(f"Missing image: {img['path']}")

        generation = article.get("generation", {})
        if generation.get("automated"):
            if article.get("evidence_status") != "verified":
                raise ValueError(f"{article['source_path']}: automated article is not verified")
            if not 2 <= len(images) <= 4:
                raise ValueError(f"{article['source_path']}: automated articles require 2-4 images")
            if not 3 <= len(article.get("quick_read", [])) <= 5:
                raise ValueError(f"{article['source_path']}: quick_read must contain 3-5 items")
            sources = article.get("sources", [])
            if len(sources) < 3:
                raise ValueError(f"{article['source_path']}: automated articles require >=3 sources")
            if not any(int(s.get("tier", 99)) == 1 for s in sources):
                raise ValueError(f"{article['source_path']}: automated articles require >=1 Tier 1 source")
            if len(article.get("body_markdown", "")) < 500:
                raise ValueError(f"{article['source_path']}: automated article body is too short")

    if not issues:
        raise ValueError("At least one issue is required")


def build_pages(articles: list[dict], issues: list[dict]) -> None:
    latest = issues[-1]
    latest_articles = latest["article_objects"]
    article_by_slug = {a["slug"]: a for a in articles}
    cover = article_by_slug.get(latest.get("cover_article"), latest_articles[0])

    render_to(
        "home.html",
        SITE / "index.html",
        root="",
        issue=latest,
        articles=latest_articles,
        cover=cover,
        site_name=SITE_NAME,
    )

    ordered = []
    for issue in issues:
        ordered.extend(issue["article_objects"])

    for i, article in enumerate(ordered):
        prev_article = ordered[(i - 1) % len(ordered)]
        next_article = ordered[(i + 1) % len(ordered)]
        issue = next(x for x in issues if article in x["article_objects"])
        article_view = dict(article)
        article_view["body_html"] = article_body_html(article, "../../")
        render_to(
            "article.html",
            SITE / "articles" / article["slug"] / "index.html",
            root="../../",
            article=article_view,
            issue=issue,
            prev_article=prev_article,
            next_article=next_article,
            site_name=SITE_NAME,
        )

    for issue in issues:
        render_to(
            "issue.html",
            SITE / "issues" / f"{int(issue['issue']):03d}" / "index.html",
            root="../../",
            issue=issue,
            articles=issue["article_objects"],
            site_name=SITE_NAME,
        )

    categories = defaultdict(list)
    tags = defaultdict(list)
    for article in articles:
        categories[article["category"]].append(article)
        for tag in article.get("tags", []):
            tags[tag].append(article)

    render_to(
        "archive.html",
        SITE / "archive" / "index.html",
        root="../",
        issues=list(reversed(issues)),
        site_name=SITE_NAME,
    )

    category_views = [
        {
            "name": name,
            "slug": items[0].get("category_slug") or slugify(name),
            "articles": items,
        }
        for name, items in categories.items()
    ]
    tag_views = [
        {
            "name": name,
            "slug": items[0].get("tag_slugs", {}).get(name) or slugify(name),
            "articles": items,
        }
        for name, items in tags.items()
    ]

    render_to(
        "collection_index.html",
        SITE / "categories" / "index.html",
        root="../",
        title="三大栏目",
        collections=category_views,
        site_name=SITE_NAME,
    )
    render_to(
        "collection_index.html",
        SITE / "tags" / "index.html",
        root="../",
        title="主题标签",
        collections=tag_views,
        site_name=SITE_NAME,
    )

    for collection in category_views:
        render_to(
            "collection.html",
            SITE / "categories" / collection["slug"] / "index.html",
            root="../../",
            title=collection["name"],
            articles=collection["articles"],
            site_name=SITE_NAME,
        )
    for collection in tag_views:
        render_to(
            "collection.html",
            SITE / "tags" / collection["slug"] / "index.html",
            root="../../",
            title=collection["name"],
            articles=collection["articles"],
            site_name=SITE_NAME,
        )

    render_to(
        "search.html",
        SITE / "search" / "index.html",
        root="../",
        site_name=SITE_NAME,
    )


def build_search(articles: list[dict]) -> None:
    index = [
        {
            "title": a["title"],
            "summary": a["summary"],
            "category": a["category"],
            "tags": a.get("tags", []),
            "date": str(a["date"]),
            "url": f"../articles/{a['slug']}/",
        }
        for a in sorted(articles, key=lambda x: x["date"], reverse=True)
    ]
    (SITE / "search_index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def build_feeds(issues: list[dict]) -> None:
    items = []
    for issue in reversed(issues[-30:]):
        date = issue["date"]
        if isinstance(date, str):
            dt = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=TZ)
        else:
            dt = datetime.combine(date, datetime.min.time(), tzinfo=TZ)
        link = SITE_URL + issue["url"]
        items.append((issue, dt, link, issue.get("daily_summary", "")))

    rss_items = "\n".join(
        f"<item><title>{escape(SITE_NAME + ' · 第' + str(int(issue['issue'])).zfill(3) + '期')}</title>"
        f"<link>{escape(link)}</link><guid>{escape(link)}</guid>"
        f"<pubDate>{format_datetime(dt)}</pubDate><description>{escape(desc)}</description></item>"
        for issue, dt, link, desc in items
    )
    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f"<rss version=\"2.0\"><channel><title>{SITE_NAME}</title>"
        f"<link>{SITE_URL}</link><description>{escape(CONFIG['description'])}</description>"
        f"{rss_items}</channel></rss>"
    )
    (SITE / "feed.xml").write_text(rss, encoding="utf-8")

    atom_entries = "\n".join(
        f"<entry><title>{escape(SITE_NAME + ' · 第' + str(int(issue['issue'])).zfill(3) + '期')}</title>"
        f"<link href=\"{escape(link)}\"/><id>{escape(link)}</id>"
        f"<updated>{dt.isoformat()}</updated><summary>{escape(desc)}</summary></entry>"
        for issue, dt, link, desc in items
    )
    updated = items[0][1].isoformat() if items else datetime.now(TZ).isoformat()
    atom = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f"<feed xmlns=\"http://www.w3.org/2005/Atom\"><title>{SITE_NAME}</title>"
        f"<id>{SITE_URL}</id><link href=\"{SITE_URL}\"/><updated>{updated}</updated>"
        f"{atom_entries}</feed>"
    )
    (SITE / "atom.xml").write_text(atom, encoding="utf-8")


def build_offline(issues: list[dict]) -> None:
    css = (STATIC / "style.css").read_text(encoding="utf-8")
    css += "\n" + (STATIC / "phase2.css").read_text(encoding="utf-8")

    for issue in issues:
        views = []
        for article in issue["article_objects"]:
            view = dict(article)
            view["body_html"] = offline_body_html(article)
            view["feature_src"] = data_uri(article["images"][0]["path"])
            views.append(view)

        html = env.get_template("offline_issue.html").render(
            issue=issue,
            articles=views,
            css=css,
            site_name=SITE_NAME,
        )
        out = SITE / "downloads" / f"issue-{int(issue['issue']):03d}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")


def main() -> None:
    ensure_clean_site()
    articles, issues = load_content()
    validate(articles, issues)
    build_pages(articles, issues)
    build_search(articles)
    build_feeds(issues)
    build_offline(issues)
    print(f"Built {len(articles)} articles and {len(issues)} issues into {SITE}")


if __name__ == "__main__":
    main()
