#!/usr/bin/env python3
"""Generate <slug>/privacy.html and <slug>/delete-account.html from _apps/<slug>.json.

  python3 _template/new_app.py billbridge

Config keys: app_name, effective_date, overview, collect[], use[], sharing, permissions[], retention,
delete_steps_html, deleted[], kept[]. Copy _apps/billbridge.json as the starting point.
"""
import json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
slug = sys.argv[1]
c = json.loads((root / "_apps" / f"{slug}.json").read_text())
li = lambda items: "\n".join(f"<li>{i}</li>" for i in items)
vals = {"app_name": c["app_name"], "effective_date": c["effective_date"], "overview": c["overview"],
        "collect_items": li(c["collect"]), "use_items": li(c["use"]), "sharing": c["sharing"],
        "permission_items": li(c["permissions"]), "retention": c["retention"],
        "delete_steps": c["delete_steps_html"], "deleted_items": li(c["deleted"]), "kept_items": li(c["kept"])}
out = root / slug
out.mkdir(exist_ok=True)
for name in ("privacy.html", "delete-account.html"):
    text = (root / "_template" / name).read_text()
    for k, v in vals.items():
        text = text.replace("{{" + k + "}}", v)
    assert "{{" not in text, f"unfilled placeholder in {name}"
    (out / name).write_text(text)
print("wrote", out)
