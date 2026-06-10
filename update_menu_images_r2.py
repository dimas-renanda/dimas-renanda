#!/usr/bin/env python3
"""
Update menu images - round 2, with verified relevant images.
All source images are local files already downloaded and verified.
"""
import json, subprocess, os, urllib.request, time

BASE_URL = "http://192.168.30.100:8080"
WS = "/Users/user/.openclaw/workspace"

# Map: menu_id -> (local_file, menu_name, price, categoryId)
# Only update menus that had wrong/irrelevant images
UPDATES = {
    "1767603514233": ("cand_hbc_a.jpg",     "Hot Black Coffee",   10000.0, "1767603417854"),
    "1767603534594": ("raw_ia_sm.jpg",       "Ice Americano",      10000.0, "1767603417854"),
    "1767603593665": ("cand_pop_a.jpg",      "Popcorn",            15000.0, "1767603424872"),
    "1767603602656": ("raw_mie1_sm.jpg",     "Mie Gelas",          15000.0, "1767603424872"),
    "1767603632225": ("raw_thai2_sm.jpg",    "Ice Thai Tea",       20000.0, "1767603417854"),
    "1767603664130": ("final_leacy_sm.jpg",  "Leacy Tea",          15000.0, "1767603417854"),
    "1767603675354": ("cand_hottea_b.jpg",   "Hot Tea",            10000.0, "1767603417854"),
    "1767603703575": ("raw_ubi_sm.jpg",      "Gowell Ubi",         10000.0, "1767603417854"),
    "1767603713714": ("final_coklat_sm.jpg", "Gowell Coklat",      10000.0, "1767603417854"),
    "1768295150047": ("final_tarik_sm.jpg",  "Teh Tarik",          25000.0, "1767603417854"),
    "1768614161743": ("cand_choco_a.jpg",    "Ice choco Malt",     20000.0, "1767603417854"),
    "1768615356045": ("raw_taro_sm.jpg",     "Ice Taro Latte",     20000.0, "1767603417854"),
    "1768615974213": ("final_vanilla_sm.jpg","Gowel Vanilla",      10000.0, "1767603417854"),
}

def upload_image(local_file):
    path = os.path.join(WS, local_file)
    result = subprocess.run(
        ["curl", "-s", "-X", "POST", f"{BASE_URL}/menu/upload-image",
         "-F", f"file=@{path}", "--max-time", "30"],
        capture_output=True, text=True
    )
    resp = json.loads(result.stdout)
    if resp.get("success"):
        return resp["data"]["imagePath"], None
    return None, resp

def update_menu(menu_id, name, price, cat_id, image_path):
    payload = {"id": menu_id, "name": name, "price": price,
               "categoryId": cat_id, "imagePath": image_path}
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/menu/update", data=data,
        headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

print("🍽️  Updating menu images (round 2 - verified relevant)\n")
ok, fail = 0, 0
for menu_id, (local_file, name, price, cat_id) in UPDATES.items():
    print(f"📌 {name}")
    image_path, err = upload_image(local_file)
    if not image_path:
        print(f"  ❌ Upload failed: {err}\n"); fail += 1; continue
    print(f"  ✅ Uploaded → {image_path}")
    res = update_menu(menu_id, name, price, cat_id, image_path)
    if res.get("success"):
        print(f"  ✅ Updated!\n"); ok += 1
    else:
        print(f"  ❌ Update failed: {res}\n"); fail += 1
    time.sleep(0.3)

print(f"{'='*50}\nDone: {ok} OK, {fail} failed")
