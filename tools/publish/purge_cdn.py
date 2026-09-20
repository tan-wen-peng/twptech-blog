# -*- coding: utf-8 -*-
"""刷新腾讯云 CDN。凭据从 ~/.cos.conf 读，绝不打印。"""
import os, re, sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

urls = sys.argv[1:] or ["https://www.twptech.site/"]
cfg = os.path.expanduser("~/.cos.conf")
txt = open(cfg, encoding="utf-8", errors="replace").read()
sid  = re.search(r"secret_id\s*=\s*(\S+)", txt).group(1)
skey = re.search(r"secret_key\s*=\s*(\S+)", txt).group(1)

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.common_client import CommonClient

cred = credential.Credential(sid, skey)
cp = ClientProfile(httpProfile=HttpProfile(endpoint="cdn.tencentcloudapi.com"))
cli = CommonClient("cdn", "2018-06-06", cred, "ap-guangzhou", profile=cp)

roots = sorted({"/".join(u.split("/")[:3]) + "/" for u in urls})
try:
    r = cli.call_json("PurgePathCache", {"Paths": roots, "FlushType": "flush"})
    print("目录刷新:", json.dumps(r, ensure_ascii=False)[:200])
except Exception as e:
    print("目录刷新失败:", str(e)[:200])

try:
    r = cli.call_json("PurgeUrlsCache", {"Urls": urls})
    print("URL 刷新:", json.dumps(r, ensure_ascii=False)[:200])
except Exception as e:
    print("URL 刷新失败:", str(e)[:200])