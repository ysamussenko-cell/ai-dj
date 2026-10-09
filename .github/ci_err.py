"""Ошибки сборки — в аннотации GitHub: их видно без скачивания логов."""
import re
import sys

PAT = re.compile(r"^e: |error:|Error:|What went wrong|FAILURE|Could not|Cannot|Unresolved|not found|"
                 r"Execution failed|Caused by|> .+|ERROR", re.I)
lines = open(sys.argv[1], encoding="utf-8", errors="replace").read().splitlines()
hits = []
for i, ln in enumerate(lines):
    if PAT.search(ln):
        hits.extend(lines[i:i + 3])
seen, out = set(), []
for h in hits:
    h = h.strip()[:300]
    if h and h not in seen:
        seen.add(h)
        out.append(h)
out = out[:60] or lines[-40:]
for k in range(0, len(out), 12):          # одна аннотация — до ~4 КБ
    chunk = "%0A".join(x.replace("%", "%25") for x in out[k:k + 12])
    print(f"::error::{chunk}")
