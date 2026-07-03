#!/bin/bash
# upload-to-cos.sh - 构建并上传 Hugo 站点到腾讯云 COS
# 用法: 编辑下方 bucket 和 region 后执行
#       cp upload-to-cos.sh upload-to-cos.local.sh
#       chmod +x upload-to-cos.local.sh
#       ./upload-to-cos.local.sh

set -e

cd "$(dirname "$0")"

BUCKET="your-bucket-12345678"    # ← 替换为你的 COS Bucket 名
REGION="ap-guangzhou"            # ← 替换为你的 COS 区域

echo "🔨 构建..."
/home/ubuntu/go/bin/hugo --minify

echo "📤 上传到 COS..."
tccli cos sync_upload \
    --bucket "$BUCKET" \
    --local_path ./public/ \
    --region "$REGION"

echo "🧹 清除 CDN 缓存..."
tccli cdn PurgeUrlsCache \
    --Urls '["https://www.yourdomain.com/*"]' 2>/dev/null || true

echo "✅ 完成！"
