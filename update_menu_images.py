#!/usr/bin/env python3
"""
Script to update menu images for TridomPantry
Uses curl for upload (reliable multipart), urllib for everything else.
"""

import json
import urllib.request
import subprocess
import tempfile
import os
import time

BASE_URL = "http://192.168.30.100:8080"

MENU_IMAGE_MAP = {
    "1767603514233": {
        "name": "Hot Black Coffee",
        "image_url": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=600&q=80",
        "filename_hint": "hot_black_coffee"
    },
    "1767603534594": {
        "name": "Ice Americano",
        "image_url": "https://images.unsplash.com/photo-1592663527359-cf6642f54cff?w=600&q=80",
        "filename_hint": "ice_americano"
    },
    "1767603559629": {
        "name": "Hot Coffee Latte",
        "image_url": "https://images.unsplash.com/photo-1561047029-3000c68339ca?w=600&q=80",
        "filename_hint": "hot_coffee_latte"
    },
    "1767603575554": {
        "name": "Ice Coffee Latte",
        "image_url": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600&q=80",
        "filename_hint": "ice_coffee_latte"
    },
    "1767603593665": {
        "name": "Popcorn",
        "image_url": "https://images.unsplash.com/photo-1606923829579-0cb981a83e2e?w=600&q=80",
        "filename_hint": "popcorn"
    },
    "1767603602656": {
        "name": "Mie Gelas",
        "image_url": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600&q=80",
        "filename_hint": "mie_gelas"
    },
    "1767603632225": {
        "name": "Ice Thai Tea",
        "image_url": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=600&q=80",
        "filename_hint": "ice_thai_tea"
    },
    "1767603664130": {
        "name": "Leacy Tea",
        "image_url": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80",
        "filename_hint": "leacy_tea"
    },
    "1767603675354": {
        "name": "Hot Tea",
        "image_url": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=600&q=80",
        "filename_hint": "hot_tea"
    },
    "1767603685479": {
        "name": "Ice Tea",
        "image_url": "https://images.unsplash.com/photo-1499638673689-79a0b5115d87?w=600&q=80",
        "filename_hint": "ice_tea"
    },
    "1767603703575": {
        "name": "Gowell Ubi",
        "image_url": "https://images.unsplash.com/photo-1501443762994-82bd5dace89a?w=600&q=80",
        "filename_hint": "gowell_ubi"
    },
    "1767603713714": {
        "name": "Gowell Coklat",
        "image_url": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=600&q=80",
        "filename_hint": "gowell_coklat"
    },
    "1768295150047": {
        "name": "Teh Tarik",
        "image_url": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80",
        "filename_hint": "teh_tarik"
    },
    "1768614161743": {
        "name": "Ice choco Malt",
        "image_url": "https://images.unsplash.com/photo-1578020190125-f4f7c18bc9cb?w=600&q=80",
        "filename_hint": "ice_choco_malt"
    },
    "1768615356045": {
        "name": "Ice Taro Latte",
        "image_url": "https://images.unsplash.com/photo-1611930022073-84b46a39e2b1?w=600&q=80",
        "filename_hint": "ice_taro_latte"
    },
    "1768615974213": {
        "name": "Gowel Vanilla",
        "image_url": "https://images.unsplash.com/photo-1534353436294-0dbd4bdac845?w=600&q=80",
        "filename_hint": "gowel_vanilla"
    },
}


def http_get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def http_post_json(url, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }, method="POST")
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def download_and_upload(image_url, filename_hint):
    """Download image to temp file, upload via curl to server."""
    # Determine extension from URL
    url_lower = image_url.split("?")[0].lower()
    if url_lower.endswith(".webp"):
        ext = "webp"
    elif url_lower.endswith(".png"):
        ext = "png"
    else:
        ext = "jpg"
    
    filename = f"{filename_hint}.{ext}"
    tmp_path = f"/tmp/{filename}"
    
    # Download with curl
    dl_result = subprocess.run(
        ["curl", "-sL", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
         image_url, "-o", tmp_path, "--max-time", "20"],
        capture_output=True, text=True
    )
    
    if dl_result.returncode != 0 or not os.path.exists(tmp_path) or os.path.getsize(tmp_path) < 1000:
        return None, f"Download failed: {dl_result.stderr}"
    
    size = os.path.getsize(tmp_path)
    print(f"  Downloaded {size} bytes → {tmp_path}")
    
    # Upload with curl
    upload_result = subprocess.run(
        ["curl", "-s", "-X", "POST",
         f"{BASE_URL}/menu/upload-image",
         "-F", f"file=@{tmp_path}",
         "--max-time", "30"],
        capture_output=True, text=True
    )
    
    if upload_result.returncode != 0:
        return None, f"Upload curl failed: {upload_result.stderr}"
    
    try:
        response = json.loads(upload_result.stdout)
    except Exception:
        return None, f"Upload response parse failed: {upload_result.stdout}"
    
    if not response.get("success"):
        return None, f"Upload error: {response}"
    
    data = response.get("data", {})
    image_path = data.get("imagePath") or data.get("path")
    
    # Cleanup temp file
    try:
        os.remove(tmp_path)
    except:
        pass
    
    return image_path, None


def get_menus():
    result = http_get_json(f"{BASE_URL}/menu")
    return {m["id"]: m for m in result["data"]}


def main():
    print("🍽️  TridomPantry Menu Image Updater\n")
    
    menus = get_menus()
    print(f"Found {len(menus)} menus\n")
    
    results = []
    
    for menu_id, info in MENU_IMAGE_MAP.items():
        if menu_id not in menus:
            print(f"⚠️  Menu ID {menu_id} ({info['name']}) not found, skipping")
            continue
        
        menu = menus[menu_id]
        print(f"📌 {info['name']} (ID: {menu_id})")
        
        # Download & upload image
        image_path, error = download_and_upload(info["image_url"], info["filename_hint"])
        
        if error:
            print(f"  ❌ {error}\n")
            results.append({"id": menu_id, "name": info["name"], "status": f"FAILED - {error}"})
            continue
        
        print(f"  ✅ Uploaded → imagePath: {image_path}")
        
        # Update menu
        try:
            update_payload = {
                "id": menu_id,
                "name": menu["name"],
                "price": menu["price"],
                "categoryId": menu["categoryId"],
                "imagePath": image_path
            }
            update_result = http_post_json(f"{BASE_URL}/menu/update", update_payload)
            
            if update_result.get("success"):
                print(f"  ✅ Menu updated!\n")
                results.append({"id": menu_id, "name": info["name"], "status": "OK", "imagePath": image_path})
            else:
                print(f"  ❌ Update failed: {update_result}\n")
                results.append({"id": menu_id, "name": info["name"], "status": f"FAILED - update: {update_result}"})
        except Exception as e:
            print(f"  ❌ Update exception: {e}\n")
            results.append({"id": menu_id, "name": info["name"], "status": f"FAILED - exception: {e}"})
        
        time.sleep(0.3)
    
    print("\n" + "="*60)
    print("📊 FINAL SUMMARY:")
    
    for r in results:
        icon = "✅" if r["status"] == "OK" else "❌"
        print(f"  {icon} {r['name']}: {r['status']}")
    
    ok = sum(1 for r in results if r["status"] == "OK")
    print(f"\n  Total: {ok} OK, {len(results)-ok} failed out of {len(results)}")


if __name__ == "__main__":
    main()
