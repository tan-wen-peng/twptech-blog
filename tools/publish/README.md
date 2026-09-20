# tools/publish — twptech.site 发布工具

配套 skill: `twptech-publish`（`~/.dsh/skills/twptech-publish/SKILL.md`）

## 一条命令发布

```bash
cd <repo>
bash tools/publish/publish.sh          # 构建 -> 上传 COS -> 刷 CDN
bash tools/publish/publish.sh --no-purge   # 只构建+上传
```

`publish.sh` 内置了两个必须的开关，**不要绕过它手写命令**：

- `MSYS_NO_PATHCONV=1` + `MSYS2_ARG_CONV_EXCL=*` —— 不加的话 Git Bash 会把 cos 路径 `/` 转成 `D:/Program Files/Git/`，整站传到错误位置且**根目录时间戳不变**，很容易误判成功。
- **绝不加 `--delete`** —— 线上 `/duck/` 分区的源码不在本仓库，删了就没了。

## 图片精修

```bash
python tools/publish/prepare_images.py <素材目录> static/images/<slug> --map <素材目录>/map.tsv
```

管线：MD5 去重 → 去 OS 标题栏 → 裁白边 → 限最长边(1440x1500) → WebP q86 → slug → 拼版验收。

映射表格式见 `map.tsv.example`（制表符分隔）。不给也能跑，但中文名会退化成 `img`/`img-2`。

**跑完只看 `contact-sheet.png`**，别逐张读图。缩略图偏小会误判，真怀疑再单独放大。

## 刷 CDN

```bash
python tools/publish/purge_cdn.py <url> [<url> ...]
```

凭据从 `~/.cos.conf` 读取，不打印。

## Hugo 从哪来

按顺序找：`$HUGO_BIN` → `D:\A_XEngineer\03_site\spring\_work\bin\hugo.exe` → `tools/publish/bin/hugo.exe` → PATH。

版本必须是 **v0.163.3 extended**（与 GitHub Actions 一致）。GitHub 直连 ~18KB/s 不可用，走镜像：

```
https://ghfast.top/https://github.com/gohugoio/hugo/releases/download/v0.163.3/hugo_extended_0.163.3_windows-amd64.zip
```

## 已知坑

详见 skill 文档 §2。最容易中的三个：

1. **frontmatter 的 `date` 晚于系统时间 → 页面静默不生成**（Hugo 默认不发布未来文章，不报错）
2. **figure shortcode 属性里用 ASCII 双引号 → 截断**，内层引号用 `「」`
3. **正文标点要全角**，半角混排一眼露馅