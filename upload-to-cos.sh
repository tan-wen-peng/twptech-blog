#!/bin/bash
# upload-to-cos.sh - 构建并上传 Hugo 站点到腾讯云 COS
# 用法: ./upload-to-cos.sh

set -e

cd "$(dirname "$0")"

echo "🔨 构建..."
/home/ubuntu/go/bin/hugo --minify

echo "📤 上传到 COS..."

tccli cos sync_upload \
    --bucket twptech-blog-1407052797 \
    --local_path ./public/ \
    --region ap-guangzhou

echo "🧹 清除 CDN 缓存..."
tccli cdn PurgeUrlsCache \
    --Urls '["https://www.twptech.site/*"]' 2>/dev/null || true

echo "✅ 完成！"
echo "➡ https://www.twptech.site/"
