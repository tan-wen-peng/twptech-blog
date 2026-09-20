#!/usr/bin/env bash
# twptech.site 发布：构建 -> 上传 COS -> 刷 CDN
# 用法: bash tools/publish/publish.sh [--no-purge] [--verify]
set -euo pipefail

# 关键①：Git Bash 会把 cos 路径 "/" 转成 "D:/Program Files/Git/"，必须关掉
export MSYS_NO_PATHCONV=1
export MSYS2_ARG_CONV_EXCL="*"

SITE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BUCKET="twptech-blog-1407052797"
BASE="https://www.twptech.site"

pick() { for c in "$@"; do [ -n "$c" ] && [ -x "$c" ] && { echo "$c"; return 0; }; done; return 1; }

HUGO_BIN="${HUGO_BIN:-$(pick \
  "/d/A_XEngineer/03_site/spring/_work/bin/hugo.exe" \
  "$SITE/tools/publish/bin/hugo.exe" \
  "$(command -v hugo 2>/dev/null || true)" || true)}"
[ -z "$HUGO_BIN" ] && { echo "!! 找不到 hugo。设 HUGO_BIN，或下载到 tools/publish/bin/hugo.exe"; exit 1; }

PY="${PYTHON_BIN:-$(pick /d/KimiCode/Scripts/python "$(command -v python 2>/dev/null || true)" || true)}"

echo "== 站点  : $SITE"
echo "== Hugo  : $HUGO_BIN"
echo "== Bucket: cos://$BUCKET/"

# 1) 构建
cd "$SITE"
"$HUGO_BIN" --minify
HTML=$(find public -name "*.html" | wc -l)
echo "== 产物  : $HTML 个 html / $(du -sh public | cut -f1)"
[ "$HTML" -lt 10 ] && { echo "!! 产物异常，中止"; exit 1; }

# 2) 上传。绝不加 --delete：线上 /duck/ 源码不在本仓库，删了就没了
echo "== 上传…"
coscmd -b "$BUCKET" upload -r ./public/ /

# 3) 刷 CDN
shopt -s nocasematch
if [ "${1:-}" != "--no-purge" ]; then
  if [ -n "$PY" ]; then
    echo "== 刷 CDN…"
    # 注意：此处必须用相对路径。MSYS_NO_PATHCONV=1 下把 MSYS 绝对路径
    # 传给 Windows Python 会被解析成 D:\d\A_XEngineer\... 而找不到文件。
    "$PY" tools/publish/purge_cdn.py "$BASE/" "$BASE/index.json" "$BASE/sitemap.xml" || \
      echo "   (CDN 刷新失败，不影响文件已上传)"
  else
    echo "== 跳过 CDN 刷新（找不到 python）"
  fi
fi

echo
echo "== 完成。验证："
echo "   curl -sI $BASE/ | grep -iE 'HTTP|x-cache|age'"
echo "   /about/ 应与线上逐字节相同；首页 diff 只应有新文章导致的差异"