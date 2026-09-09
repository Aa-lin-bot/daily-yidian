# 《每天亿点小知识》自动生产契约 v1

本文件规定 ChatGPT 定时任务与 GitHub Pages 构建器之间的接口。自动任务必须严格遵守。

## 1. 两阶段发布

- 18:00（Asia/Shanghai）：只写入 `drafts/YYYY/MM/DD/` 和 `reports/fact_checks/`，不得写入 `content/`。
- 20:00（Asia/Shanghai）：复核当天草稿，通过后复制到 `content/YYYY/MM/DD/`。只有 `content/` 会进入网站。
- 草稿提交不会触发 Pages；正式内容提交会触发 Pages。

## 2. 每期文件

```text
drafts/YYYY/MM/DD/
├─ issue.yml
├─ article-01.md
├─ article-02.md
└─ article-03.md   # 当天只有2篇时可省略
```

正式发布时保持相同文件名复制到 `content/YYYY/MM/DD/`。

## 3. 选题

- 每天 2–3 篇。
- 栏目：宇宙与地球 / 生命与自然 / 人类与科学。
- 长期目标：经典百科约 80%，近期可靠的新发现约 20%。
- 参考过去 180 天 `content/`，避免同一核心问题重复。
- 不追逐未经充分证实的热点；争议性问题必须明确证据边界。

## 4. 事实标准

每篇必须：

- 至少 3 个独立信息来源。
- 至少 1 个 Tier 1 来源：原始论文、政府/国家科研机构、科研数据库、NASA/ESA/NOAA/USGS/IUCN 等同等级来源。
- 关键数字、年代、机制和因果关系必须可追溯。
- 来源发生冲突时不得自行猜测；若无法解决，换题。
- `evidence_status: verified` 仅在完成逐条核验后填写。
- 800–1500 中文字为常规目标；复杂主题可适当增加。
- 文章面向成年人认知提升，语言通俗但不得牺牲准确性。

## 5. 自动文章 Front Matter 必填

```yaml
id: YYYY-MM-DD-NNN
date: YYYY-MM-DD
issue: 2
title: ...
slug: english-kebab-case
category: 宇宙与地球
category_slug: universe-earth
tags: [...]
tag_slugs: {...}
difficulty: 入门
reading_minutes: 7
summary: ...
quick_read:
  - ...
  - ...
  - ...
evidence_status: verified

images:
  - path: assets/images/YYYY/MM/DD/unique-file.jpg
    download_url: https://可直接下载的图片地址
    original_url: https://图片来源说明页
    alt: 客观中文替代文本
    caption: 图片实际内容
    credit: 作者或机构
    license: 精确许可证名称

sources:
  - title: ...
    organization: ...
    url: ...
    tier: 1
    accessed: YYYY-MM-DD

quiz:
  - question: ...
    options: [A, B, C]
    answer: 0
    explanation: ...

generation:
  source: chatgpt-automation
  automated: true
  pipeline_version: "3.0"
```

## 6. 图片规则

- 自动文章每篇必须 2–4 张图片。
- 优先真实的开放授权或公有领域科学图片。
- Wikimedia Commons、NASA、NOAA、USGS、ESA、博物馆/科研机构开放资源优先。
- 必须实际打开图片说明页核对作者/机构和许可证，不能凭文件名猜许可证。
- `download_url` 必须是无需登录即可由 GitHub Actions 下载的直接图片 URL；不能填写普通网页地址。
- `original_url` 必须指向图片说明/授权页面。
- `path` 必须位于 `assets/images/YYYY/MM/DD/`，文件名不得与历史图片冲突。
- 不把远程图片直接展示给终端浏览器；GitHub Actions 会先下载，再由 GitHub Pages 本地提供。
- 如果找不到授权明确且可自动下载的合适图片，优先换图；仍无法满足则换题，不得杜撰许可证。

## 7. 正文结构

正文 Markdown 不生成“文章目录”。页面模板不会展示目录。

建议结构：
- 30 秒速读由 Front Matter 的 `quick_read` 生成
- 3–5 个正文小节
- 必要时使用数据/事实提示框
- 在正文中用 `[[image:1]]`、`[[image:2]]` 插入第2、第3张图（索引从0开始；第1张图自动作为头图）
- 结尾 2–3 道小测验
- 核心来源由 Front Matter 自动渲染

## 8. 事实核验报告

18:00 草稿任务同时写：

`reports/fact_checks/YYYY-MM-DD.json`

至少记录每篇的核心事实、核验状态、支持来源和无法确认的事项。报告不展示到前台。

## 9. 失败策略

- 计划 3 篇但仅 2 篇达到标准：发布 2 篇。
- 少于 2 篇达到标准：当天不发布新一期。
- 禁止用前一天内容补位。
- 禁止为了达到篇数降低来源或图片许可标准。

## 10. 幂等性

自动任务每次运行前必须检查目标日期是否已存在：
- 18:00：已有完整草稿时不得重复生成另一期。
- 20:00：当天 `content/` 已存在时不得重复发布。
