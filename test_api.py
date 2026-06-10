#!/usr/bin/env python3
"""
TriDominic API Test Script (v202604)
Domain: tridom.biz.id
"""

import json
import requests
import sys
from datetime import datetime

# CONFIG
DOMAIN = "tridom.biz.id"
BASE_URL = f"https://{DOMAIN}"
TOKEN = "eyJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6IkRJTUFTUkVOQU5EQVNPRllBTiIsImV4cCI6MTkzMzM4ODMxMCwiaWF0IjoxNzc3ODY4MzEwfQ.4QDrojjdIk_qS4-TKEWmALlTL71BRbuYFea7x7B3oCeN7zM-w-lERS82CJHVd_CjJ_GELUd8LqZ0GoZFTXlZbi2DChnDo60NIdJDsYmGXJHuL4Ku3xyB1x_1I9rf2Z7gqFXlSxktfW2Sm5JmTLkkJw-NZUFCCizb41tiU-5DI6kei7LgYFS2A-xqmwtDRwMGH_06BwrLYOrbq7BXPLQmYaEXDoU27YlnYcXY4kVC-rq6wKN6SJAJ3IwAwLb4xTHsTumMn0ThAJ7giOKSxul42kiXrYy_HUnTSRqBRoH8STgEETyw2xR3hb7zuFaicpIWN7TQX7epbpcufGKsbh7LKLK8YnRAlLduRDMBqFmYoIcGIRMRohbSTRbxEiCsKUMf49yzLQXBPeXn43FohT6rfQ1KCoFTFw9nVqxwO_T5OZAMUfDNSZiCkOqenlo2IFOJXgb9u_jIb7UoxB5sMWdtF11xcGNMtWHQeI1acj3CYw1nIdTIQzhMszrJqA-hlrprt9C7qMdObQxwBZaP93daS8KTw5Rb3aPcot06fZKU7F-X1T-xqE__VAXw3wDBx_tX2c5O-j6Y_yr1QY664CecBpqDH59x1TdogM718a3fSj9J5PxS0Y_BfU30Kr9H2oO8kMWNzkR1_ExXg4jA8YByhZj3BktgySK6EB3xfSywv3c"  # <-- REPLACE THIS

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# API Test Data (92 unique modulCode)
API_TESTS = [
    # USER & AUTH
    ("getSnituser", {"modulCode": "getSnituser", "additionalBody": {}}),
    ("saveUserBs", {"modulCode": "saveUserBs", "additionalBody": {"userId": "1", "bs": "BS01"}}),
    ("saveUserEnabled", {"modulCode": "saveUserEnabled", "additionalBody": {"id": "1", "enabled": "true"}}),
    ("resetImei", {"modulCode": "resetImei", "additionalBody": {"id": "1"}}),
    ("resetPassword", {"modulCode": "resetPassword", "additionalBody": {"id": "1"}}),
    ("enableBs", {"modulCode": "enableBs", "additionalBody": {"id": "1", "bs": "BS01"}}),
    ("getLokasi", {"modulCode": "getLokasi", "additionalBody": {}}),
    ("saveSnituserLokasi", {"modulCode": "saveSnituserLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}),
    
    # TRUCK
    ("getTruck", {"modulCode": "getTruck", "additionalBody": {}}),
    ("resetNfc", {"modulCode": "resetNfc", "additionalBody": {"id": "1"}}),
    ("saveTruckAvailable", {"modulCode": "saveTruckAvailable", "additionalBody": {"id": "1", "available": "true"}}),
    ("saveTruckLokasi", {"modulCode": "saveTruckLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}),
    ("saveNfcTruck", {"modulCode": "saveNfcTruck", "additionalBody": {"id": "1", "nfc": "NFC001", "platNo": "B 1234 ABC"}}),
    
    # INVENTORY
    ("invGetItemStockOpname", {"modulCode": "invGetItemStockOpname", "additionalBody": {}}),
    ("invGetSite", {"modulCode": "invGetSite", "additionalBody": {}}),
    ("invGetItem", {"modulCode": "invGetItem", "additionalBody": {}}),
    ("saveInventoryAvailable", {"modulCode": "saveInventoryAvailable", "additionalBody": {"id": "1", "available": "true"}}),
    ("saveInventoryLokasi", {"modulCode": "saveInventoryLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}),
    ("saveNfcInventory", {"modulCode": "saveNfcInventory", "additionalBody": {"id": "1", "nfc": "NFC001", "inventoryNo": "INV001"}}),
    ("invDeleteItemStockOpname", {"modulCode": "invDeleteItemStockOpname", "additionalBody": {"id": "1"}}),
    ("invSaveItemStockOpname", {"modulCode": "invSaveItemStockOpname", "additionalBody": {"itemId": "1", "quantity": 100}}),
    
    # GENSET
    ("getGenset", {"modulCode": "getGenset", "additionalBody": {}}),
    ("saveGensetAvailable", {"modulCode": "saveGensetAvailable", "additionalBody": {"id": "1", "available": "true"}}),
    ("saveGensetLokasi", {"modulCode": "saveGensetLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}),
    ("saveNfcGenset", {"modulCode": "saveNfcGenset", "additionalBody": {"id": "1", "nfc": "NFC001", "gensetNo": "GS001"}}),
    
    # SASIS
    ("getSasis", {"modulCode": "getSasis", "additionalBody": {}}),
    ("saveSasisAvailable", {"modulCode": "saveSasisAvailable", "additionalBody": {"id": "1", "available": "true"}}),
    ("saveSasisLokasi", {"modulCode": "saveSasisLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}),
    ("saveNfcSasis", {"modulCode": "saveNfcSasis", "additionalBody": {"id": "1", "nfc": "NFC001", "sasisNo": "SS001"}}),
    
    # ASSET
    ("getAsset", {"modulCode": "getAsset", "additionalBody": {}}),
    ("saveNfcAsset", {"modulCode": "saveNfcAsset", "additionalBody": {"id": "1", "nfc": "NFC001", "assetName": "Asset 01"}}),
    
    # DRIVER
    ("getDriver", {"modulCode": "getDriver", "additionalBody": {}}),
    ("saveDriverEnabled", {"modulCode": "saveDriverEnabled", "additionalBody": {"id": 1, "enabled": True}}),
    ("saveDriverStatus", {"modulCode": "saveDriverStatus", "additionalBody": {"id": 1, "status": "active"}}),
    ("getDriverName", {"modulCode": "getDriverName", "additionalBody": {}}),
    
    # DRIVER ORDER
    ("toGetDriverJob", {"modulCode": "toGetDriverJob", "additionalBody": {}}),
    ("toSaveDriverJobTruckPlatNo", {"modulCode": "toSaveDriverJobTruckPlatNo", "additionalBody": {"id": "1", "platNo": "B 1234 ABC"}}),
    ("toSaveDriverJobSasisNo", {"modulCode": "toSaveDriverJobSasisNo", "additionalBody": {"id": "1", "sasisNo": "SS001"}}),
    ("toSaveDriverJobGensetNo", {"modulCode": "toSaveDriverJobGensetNo", "additionalBody": {"id": "1", "gensetNo": "GS001"}}),
    ("toSaveDriverJob", {"modulCode": "toSaveDriverJob", "additionalBody": {"id": "1", "driverId": "1"}}),
    
    # ADMIN TRUCK
    ("toSaveDriver", {"modulCode": "toSaveDriver", "additionalBody": {"id": "1", "driverId": "1"}}),
    ("toSaveTrxType", {"modulCode": "toSaveTrxType", "additionalBody": {"id": "1", "trxType": "IN"}}),
    ("toSaveDriverLuar", {"modulCode": "toSaveDriverLuar", "additionalBody": {"id": "1", "driverId": "1"}}),
    
    # POM
    ("getPom", {"modulCode": "getPom", "additionalBody": {}}),
    ("savePomEnabled", {"modulCode": "savePomEnabled", "additionalBody": {"id": "1", "enabled": True}}),
    ("resetPumpNfc", {"modulCode": "resetPumpNfc", "additionalBody": {"id": "1"}}),
    ("saveNfcPom", {"modulCode": "saveNfcPom", "additionalBody": {"id": "1", "nfc": "NFC001", "machineName": "POM 01"}}),
    ("NfcCheckMesin", {"modulCode": "NfcCheckMesin", "additionalBody": {"idmesin": "MESIN001"}}),
    ("savePomStock", {"modulCode": "savePomStock", "additionalBody": {"id": "1", "stock": 100}}),
    
    # BS
    ("bsCheckUser", {"modulCode": "bsCheckUser", "additionalBody": {}}),
    ("bsGetVerify", {"modulCode": "bsGetVerify", "additionalBody": {}}),
    ("bsGetDone", {"modulCode": "bsGetDone", "additionalBody": {}}),
    ("bsSavePass", {"modulCode": "bsSavePass", "additionalBody": {"password": "password123"}}),
    ("bsGetSnituser", {"modulCode": "bsGetSnituser", "additionalBody": {}}),
    ("bsGetPass", {"modulCode": "bsGetPass", "additionalBody": {}}),
    ("bsGetApproval", {"modulCode": "bsGetApproval", "additionalBody": {}}),
    ("bsSaveApproval", {"modulCode": "bsSaveApproval", "additionalBody": {"id": "1", "approval": "approved"}}),
    ("bsGetRepoApproval", {"modulCode": "bsGetRepoApproval", "additionalBody": {}}),
    ("bsGetJO", {"modulCode": "bsGetJO", "additionalBody": {"jo": "JO001"}}),
    ("bsGetAmount", {"modulCode": "bsGetAmount", "additionalBody": {"jo": "JO001", "jenis": "EXPORT"}}),
    ("bsGetVessel", {"modulCode": "bsGetVessel", "additionalBody": {}}),
    ("bsGetReal", {"modulCode": "bsGetReal", "additionalBody": {"jo": "JO001", "vessel": "VES01"}}),
    ("bsGetTO", {"modulCode": "bsGetTO", "additionalBody": {"jo": "JO001", "jenis": "EXPORT", "realisasi": "REAL01"}}),
    ("bsGetDepoLuar", {"modulCode": "bsGetDepoLuar", "additionalBody": {}}),
    
    # AP
    ("apCheckUser", {"modulCode": "apCheckUser", "additionalBody": {}}),
    ("apGetVendor", {"modulCode": "apGetVendor", "additionalBody": {"jenis": "VENDOR"}}),
    ("apGetData", {"modulCode": "apGetData", "additionalBody": {"jo": "JO001", "jenis": "IMPORT"}}),
    ("apGetJO", {"modulCode": "apGetJO", "additionalBody": {"jo": "JO001"}}),
    
    # DASHBOARD
    ("dashboardCheckUser", {"modulCode": "dashboardCheckUser", "additionalBody": {}}),
    ("dashboardIN", {"modulCode": "dashboardIN", "additionalBody": {"lokasi": "Jakarta"}}),
    ("dashboardStripping", {"modulCode": "dashboardStripping", "additionalBody": {"lokasi": "Jakarta"}}),
    ("dashboardStuffing", {"modulCode": "dashboardStuffing", "additionalBody": {"lokasi": "Jakarta"}}),
    ("dashboardStrippingUpdate", {"modulCode": "dashboardStrippingUpdate", "additionalBody": {"id": "1", "status": "done", "containerNo": "CONT001"}}),
    ("dashboardStuffingUpdate", {"modulCode": "dashboardStuffingUpdate", "additionalBody": {"id": "1", "status": "done", "containerNo": "CONT001"}}),
    
    # SALES
    ("getSales", {"modulCode": "getSales", "additionalBody": {}}),
    ("getCustomer", {"modulCode": "getCustomer", "additionalBody": {"sales": "SALES01"}}),
    ("saveCustomerBlacklist", {"modulCode": "saveCustomerBlacklist", "additionalBody": {"customerId": "1", "status": "blacklist"}}),
    
    # PANTRY
    ("pantryGetSaldo", {"modulCode": "pantryGetSaldo", "additionalBody": {}}),
    ("pantryGetOrder", {"modulCode": "pantryGetOrder", "additionalBody": {}}),
    ("pantrySaveOrder", {"modulCode": "pantrySaveOrder", "additionalBody": {"orderData": {"items": [], "total": 0}}}),
    ("pantryCancelOrder", {"modulCode": "pantryCancelOrder", "additionalBody": {"orderId": "1"}}),
    
    # PATROL
    ("patrolGetData", {"modulCode": "patrolGetData", "additionalBody": {}}),
    ("patrolCompleteTask", {"modulCode": "patrolCompleteTask", "additionalBody": {"taskId": "1", "completedAt": "2026-05-05T10:00:00Z"}}),
    
    # POM USER
    ("pomGetPomLog", {"modulCode": "pomGetPomLog", "additionalBody": {"doctype": "POM_OUT"}}),
    ("pomGetPomLogNew", {"modulCode": "pomGetPomLogNew", "additionalBody": {"doctype": "POM_OUT"}}),
    ("pomSavePomLog", {"modulCode": "pomSavePomLog", "additionalBody": {"id": "1", "qty": "10", "keterangan": "Test"}}),
    ("pomSavePomLogDone", {"modulCode": "pomSavePomLogDone", "additionalBody": {"id": "1"}}),
    ("pomStartRequest", {"modulCode": "pomStartRequest", "additionalBody": {"pomId": "1", "qty": "10"}}),
    
    # ACCIDENT
    ("taGetAccident", {"modulCode": "taGetAccident", "additionalBody": {"accidentType": "TRUCK"}}),
    ("taApprovalAccident", {"modulCode": "taApprovalAccident", "additionalBody": {"id": "1", "action": "approve"}}),
    ("taDeleteAccident", {"modulCode": "taDeleteAccident", "additionalBody": {"id": "1"}}),
    ("taRequestApprovalAccident", {"modulCode": "taRequestApprovalAccident", "additionalBody": {"id": "1"}}),
    ("toGetAccident", {"modulCode": "toGetAccident", "additionalBody": {}}),
    ("toApproveAccident", {"modulCode": "toApproveAccident", "additionalBody": {"id": "1", "approval": "approved"}}),
    ("getContainer", {"modulCode": "getContainer", "additionalBody": {}}),
    
    # SECURITY GATE
    ("sgGetGateLog", {"modulCode": "sgGetGateLog", "additionalBody": {}}),
    ("sgGetTO", {"modulCode": "sgGetTO", "additionalBody": {}}),
    
    # VESSEL
    ("getVesselName", {"modulCode": "getVesselName", "additionalBody": {}}),
    ("getVesselSchedule", {"modulCode": "getVesselSchedule", "additionalBody": {"port": "Jakarta", "eta": "2026-05-10"}}),
    ("getPortOrigin", {"modulCode": "getPortOrigin", "additionalBody": {"vessel": "VES01"}}),
    ("getPortDestination", {"modulCode": "getPortDestination", "additionalBody": {"vessel": "VES01"}}),
    
    # SIMULATE
    ("bsSimulasiGetJO", {"modulCode": "bsSimulasiGetJO", "additionalBody": {"jo": "JO001"}}),
    ("bsSimulasiGetAmount", {"modulCode": "bsSimulasiGetAmount", "additionalBody": {"jo": "JO001", "jenis": "EXPORT"}}),
    
    # PLUG
    ("plugGetPlugLog", {"modulCode": "plugGetPlugLog", "additionalBody": {"doctype": "OUT"}}),
    ("plugSavePlugLog", {"modulCode": "plugSavePlugLog", "additionalBody": {"id": "1", "qty": "10"}}),
    ("checkPlugJo", {"modulCode": "checkPlugJo", "additionalBody": {"docNo": "DOC001"}}),
    
    # LIFECYCLE
    ("saveUserHeartbeat", {"modulCode": "saveUserHeartbeat", "additionalBody": {"lat": "-6.200000", "lng": "106.816666", "accuracy": "10.0"}}),
    ("killHeartbeat", {"modulCode": "killHeartbeat", "additionalBody": {"imei": "123456789012345"}}),
    
    # CHECK NFC
    ("checkNfc", {"modulCode": "checkNfc", "additionalBody": {"nfc": "NFC001"}}),
]

def test_api(name, payload):
    """Test a single API endpoint"""
    url = f"{BASE_URL}/api/snit"
    
    # Add appVersion to payload
    payload["appVersion"] = "202604"
    
    try:
        response = requests.post(url, json=payload, headers=HEADERS, timeout=30)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("success") == True:
                    return {"status": "✅ SUCCESS", "code": response.status_code, "message": data.get("message", "")}
                else:
                    return {"status": "⚠️  API ERROR", "code": response.status_code, "message": data.get("message", "Unknown error")}
            except:
                return {"status": "⚠️  PARSE ERROR", "code": response.status_code, "message": "Response bukan JSON"}
        elif response.status_code == 401:
            return {"status": "❌ UNAUTHORIZED", "code": response.status_code, "message": "Token invalid"}
        elif response.status_code == 404:
            return {"status": "❌ NOT FOUND", "code": response.status_code, "message": "Endpoint tidak ditemukan"}
        elif response.status_code == 500:
            return {"status": "❌ SERVER ERROR", "code": response.status_code, "message": "Server error"}
        else:
            return {"status": f"⚠️  HTTP {response.status_code}", "code": response.status_code, "message": ""}
            
    except requests.exceptions.Timeout:
        return {"status": "❌ TIMEOUT", "code": 0, "message": "Request timeout"}
    except requests.exceptions.ConnectionError:
        return {"status": "❌ CONNECTION ERROR", "code": 0, "message": "Tidak dapat connect ke server"}
    except Exception as e:
        return {"status": "❌ ERROR", "code": 0, "message": str(e)}

def main():
    print("=" * 60)
    print("TriDominic API Test Script")
    print(f"Domain: {DOMAIN}")
    print(f"Total APIs: {len(API_TESTS)}")
    print("=" * 60)
    print()
    
    # Check if token is replaced
    if TOKEN == "REPLACE_WITH_YOUR_TOKEN_HERE":
        print("⚠️  ERROR: Please replace TOKEN variable with your actual bearer token!")
        print("   Edit file: /Users/user/.openclaw/workspace/test_api.py")
        print("   Line: TOKEN = 'REPLACE_WITH_YOUR_TOKEN_HERE'")
        print()
        sys.exit(1)
    
    # Test all APIs
    results = []
    success_count = 0
    error_count = 0
    
    for i, (name, payload) in enumerate(API_TESTS, 1):
        result = test_api(name, payload)
        results.append((name, result))
        
        if "SUCCESS" in result["status"]:
            success_count += 1
            icon = "✅"
        elif "UNAUTHORIZED" in result["status"]:
            error_count += 1
            icon = "❌"
        else:
            error_count += 1
            icon = "⚠️"
        
        print(f"[{i:02d}/{len(API_TESTS)}] {icon} {name}")
        print(f"         Status: {result['status']} | Code: {result['code']}")
        if result["message"]:
            print(f"         Message: {result['message'][:80]}...")
        print()
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total APIs Tested: {len(API_TESTS)}")
    print(f"✅ Success: {success_count}")
    print(f"❌ Error: {error_count}")
    print(f"Success Rate: {(success_count/len(API_TESTS)*100):.1f}%")
    print("=" * 60)
    
    # Save results to file
    output_file = "/Users/user/.openclaw/workspace/api_test_results.txt"
    with open(output_file, "w") as f:
        f.write(f"TriDominic API Test Results\n")
        f.write(f"Domain: {DOMAIN}\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write(f"App Version: 202604\n")
        f.write("=" * 60 + "\n\n")
        
        for name, result in results:
            status_icon = "✅" if "SUCCESS" in result["status"] else "❌"
            f.write(f"{status_icon} {name}\n")
            f.write(f"    Status: {result['status']} | HTTP Code: {result['code']}\n")
            if result["message"]:
                f.write(f"    Message: {result['message']}\n")
            f.write("\n")
        
        f.write("=" * 60 + "\n")
        f.write(f"Summary: {success_count} Success, {error_count} Error\n")
    
    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()