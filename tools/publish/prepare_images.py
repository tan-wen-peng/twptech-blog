# -*- coding: utf-8 -*-
"""图片精修管线：去 OS 标题栏 -> 裁白边 -> 限最长边 -> WebP -> 英文 slug

用法:
    python prepare_images.py <源目录> <输出目录> [选项]

选项:
    --map map.tsv      每行 "原文件名<TAB>slug[<TAB>顶部裁掉像素]"，可省
    --titlebar auto    宽度>=2000 时自动裁掉顶部 2.25%（默认 auto）
    --titlebar none    不裁标题栏
    --max 1440x1500    输出上限（默认）
    --quality 86       WebP 质量

没有 --map 时自动去重(MD5)并生成 slug（数字前缀 + 去中文的 ASCII 残部）。
输出目录会生成 contact-sheet.png 供一次性验收，以及 manifest.json。
"""
import os, sys, json, hashlib, argparse
from PIL import Image, ImageChops, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--map", default=None)
ap.add_argument("--titlebar", default="auto")
ap.add_argument("--max", default="1440x1500")
ap.add_argument("--quality", type=int, default=86)
ap.add_argument("--tol", type=int, default=14)
a = ap.parse_args()

MAXW, MAXH = (int(x) for x in a.max.lower().split("x"))
PAD_PCT, PAD_MIN, MAX_UP = 0.06, 8, 2.0
EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff"}
os.makedirs(a.out, exist_ok=True)

def auto_slug(name, used):
    stem = os.path.splitext(name)[0]
    keep = "".join(c if (c.isascii() and (c.isalnum() or c in "-_")) else " " for c in stem)
    parts = [p for p in keep.replace("_", " ").split() if p]
    s = "-".join(parts).lower().strip("-") or "img"
    n, base = 2, s
    while s in used:
        s = base + "-" + str(n); n += 1
    return s

def bbox_content(im, tol):
    w, h = im.size; rgb = im.convert("RGB"); px = rgb.load()
    cs = [px[1,1], px[w-2,1], px[1,h-2], px[w-2,h-2]]
    bg = tuple(sum(c[i] for c in cs)//4 for i in range(3))
    m = ImageChops.difference(rgb, Image.new("RGB",(w,h),bg)).convert("L")
    bb = m.point(lambda p: 255 if p > tol else 0).getbbox()
    if not bb: return (0,0,w,h)
    l,t,r,b = bb
    px_, py_ = max(PAD_MIN,int((r-l)*PAD_PCT)), max(PAD_MIN,int((b-t)*PAD_PCT))
    return (max(0,l-px_), max(0,t-py_), min(w,r+px_), min(h,b+py_))

# 读 map
mapping = {}
if a.map and os.path.exists(a.map):
    for line in open(a.map, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#"): continue
        f = line.split("\t")
        if len(f) >= 2: mapping[f[0].strip()] = (f[1].strip(), int(f[2]) if len(f) > 2 and f[2].strip().isdigit() else None)

files = sorted(f for f in os.listdir(a.src) if os.path.splitext(f)[1].lower() in EXTS)
if not files: sys.exit("源目录没有图片: " + a.src)

seen_md5, used, man = {}, set(), []
for name in files:
    p = os.path.join(a.src, name)
    digest = hashlib.md5(open(p, "rb").read()).hexdigest()
    if digest in seen_md5:
        print("SKIP 重复: %s  (同 %s)" % (name, seen_md5[digest])); continue
    seen_md5[digest] = name

    if name in mapping: slug, top = mapping[name]
    else: slug, top = auto_slug(name, used), None
    if slug in used: print("WARN slug 冲突: " + slug); slug = auto_slug(slug, used)
    used.add(slug)

    im = Image.open(p); im.load(); fmt = im.format; im = im.convert("RGB")
    W0, H0 = im.size
    if top is None and a.titlebar == "auto" and W0 >= 2000:
        top = round(H0 * 0.0225)
    if top: im = im.crop((0, top, W0, H0))
    im = im.crop(bbox_content(im, a.tol))
    w, h = im.size
    s = min(MAXW/w, MAXH/h, MAX_UP)
    if abs(s-1) > 0.02:
        im = im.resize((max(1,round(w*s)), max(1,round(h*s))), Image.LANCZOS)
    o = os.path.join(a.out, slug + ".webp")
    im.save(o, "WEBP", quality=a.quality, method=6)
    man.append(dict(slug=slug, src=name, fmt=fmt, orig=[W0,H0], out=list(im.size), bytes=os.path.getsize(o)))
    print("%-24s %s %dx%d -> %dx%d  %dKB" % (slug, fmt, W0, H0, im.size[0], im.size[1], os.path.getsize(o)//1024))

json.dump(man, open(os.path.join(a.out,"manifest.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)

COLS, CW, CH, PADT = 6, 300, 210, 22
rows = (len(man)+COLS-1)//COLS
sheet = Image.new("RGB", (COLS*(CW+8)+8, rows*(CH+PADT+8)+8), (245,246,248))
d = ImageDraw.Draw(sheet)
try: font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
except Exception: font = ImageFont.load_default()
for i, m in enumerate(man):
    t = Image.open(os.path.join(a.out, m["slug"]+".webp")).convert("RGB")
    t.thumbnail((CW, CH), Image.LANCZOS)
    cx, cy = 8+(i%COLS)*(CW+8), 8+(i//COLS)*(CH+PADT+8)
    sheet.paste(t, (cx+(CW-t.width)//2, cy+(CH-t.height)//2))
    d.text((cx, cy+CH+3), "%d. %s" % (i+1, m["slug"]), fill=(30,30,30), font=font)
sheet.save(os.path.join(a.out, "contact-sheet.png"))
print("")
print("完成 %d 张 -> %s" % (len(man), a.out))
print("拼版: " + os.path.join(a.out, "contact-sheet.png"))