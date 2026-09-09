# 每天亿点小知识

个人长期科普电子杂志。

当前阶段：Phase 2 自动构建层。

内容源从手写 HTML 迁移为 content/YYYY/MM/DD/issue.yml 与 article-xx.md。

GitHub Actions 自动执行：Markdown + YAML → Python/Jinja2 → 首页 → 期刊页 → 单篇文章页 → 分类/标签 → 往期归档 → 搜索索引 → RSS/Atom → Base64 图片离线 HTML → GitHub Pages。

本地构建：先安装 requirements.txt，再执行 python build.py。构建产物位于 site/，不需要提交到仓库。

下一阶段：接入 ChatGPT 定时任务，使每天的新一期内容按同一 Markdown/YAML 结构自动提交到仓库，随后由本构建流水线自动发布。
