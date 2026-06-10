#!/bin/bash

# TriDominic API Test Script (v202604)
# Domain: tridom.biz.id
# Note: Replace TOKEN with your actual bearer token

DOMAIN="tridom.biz.id"
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMSIsInVzZXJuYW1lIjoiYWRtaW4iLCJpYXQiOjE3NDU2NzQwMDB9.EXAMPLE"
BASE_URL="https://$DOMAIN"

echo "=========================================="
echo "TriDominic API Test - $(date)"
echo "Domain: $DOMAIN"
echo "=========================================="
echo ""

# Function to test API
test_api() {
    local name=$1
    local modulcode=$2
    local body=$3
    
    echo "Testing: $name"
    echo "modulCode: $modulcode"
    
    response=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "$BASE_URL/api/snit" \
        -H "Authorization: Bearer $TOKEN" \
        -H "Content-Type: application/json" \
        -d "$body" 2>/dev/null)
    
    http_code=$(echo "$response" | grep "HTTP_CODE:" | cut -d: -f2)
    response_body=$(echo "$response" | sed '/HTTP_CODE:/d')
    
    if [ "$http_code" = "200" ]; then
        echo "✅ Status: $http_code - SUCCESS"
    elif [ "$http_code" = "401" ]; then
        echo "❌ Status: $http_code - UNAUTHORIZED (check token)"
    elif [ "$http_code" = "404" ]; then
        echo "❌ Status: $http_code - NOT FOUND"
    elif [ "$http_code" = "500" ]; then
        echo "❌ Status: $http_code - SERVER ERROR"
    else
        echo "⚠️  Status: $http_code"
    fi
    echo "Response: ${response_body:0:200}..."
    echo "---"
}

# ================== USER & AUTH ==================
echo "=========================================="
echo "SECTION 1: USER & AUTH"
echo "=========================================="

test_api "Get Snituser" "getSnituser" '{"appVersion": "202604", "modulCode": "getSnituser", "additionalBody": {}}'

test_api "Save User BS" "saveUserBs" '{"appVersion": "202604", "modulCode": "saveUserBs", "additionalBody": {"userId": "1", "bs": "BS01"}}'

test_api "Save User Enabled" "saveUserEnabled" '{"appVersion": "202604", "modulCode": "saveUserEnabled", "additionalBody": {"id": "1", "enabled": "true"}}'

test_api "Reset IMEI" "resetImei" '{"appVersion": "202604", "modulCode": "resetImei", "additionalBody": {"id": "1"}}'

test_api "Reset Password" "resetPassword" '{"appVersion": "202604", "modulCode": "resetPassword", "additionalBody": {"id": "1"}}'

test_api "Enable BS" "enableBs" '{"appVersion": "202604", "modulCode": "enableBs", "additionalBody": {"id": "1", "bs": "BS01"}}'

test_api "Get Lokasi" "getLokasi" '{"appVersion": "202604", "modulCode": "getLokasi", "additionalBody": {}}'

test_api "Save Snituser Lokasi" "saveSnituserLokasi" '{"appVersion": "202604", "modulCode": "saveSnituserLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}'

# ================== TRUCK ==================
echo "=========================================="
echo "SECTION 2: TRUCK"
echo "=========================================="

test_api "Get Truck" "getTruck" '{"appVersion": "202604", "modulCode": "getTruck", "additionalBody": {}}'

test_api "Reset NFC" "resetNfc" '{"appVersion": "202604", "modulCode": "resetNfc", "additionalBody": {"id": "1"}}'

test_api "Save Truck Available" "saveTruckAvailable" '{"appVersion": "202604", "modulCode": "saveTruckAvailable", "additionalBody": {"id": "1", "available": "true"}}'

test_api "Save Truck Lokasi" "saveTruckLokasi" '{"appVersion": "202604", "modulCode": "saveTruckLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}'

test_api "Save NFC Truck" "saveNfcTruck" '{"appVersion": "202604", "modulCode": "saveNfcTruck", "additionalBody": {"id": "1", "nfc": "NFC001", "platNo": "B 1234 ABC"}}'

# ================== INVENTORY ==================
echo "=========================================="
echo "SECTION 3: INVENTORY"
echo "=========================================="

test_api "Get Item Stock Opname" "invGetItemStockOpname" '{"appVersion": "202604", "modulCode": "invGetItemStockOpname", "additionalBody": {}}'

test_api "Get Site" "invGetSite" '{"appVersion": "202604", "modulCode": "invGetSite", "additionalBody": {}}'

test_api "Get Item" "invGetItem" '{"appVersion": "202604", "modulCode": "invGetItem", "additionalBody": {}}'

test_api "Save Inventory Available" "saveInventoryAvailable" '{"appVersion": "202604", "modulCode": "saveInventoryAvailable", "additionalBody": {"id": "1", "available": "true"}}'

test_api "Save Inventory Lokasi" "saveInventoryLokasi" '{"appVersion": "202604", "modulCode": "saveInventoryLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}'

test_api "Save NFC Inventory" "saveNfcInventory" '{"appVersion": "202604", "modulCode": "saveNfcInventory", "additionalBody": {"id": "1", "nfc": "NFC001", "inventoryNo": "INV001"}}'

test_api "Delete Item Stock Opname" "invDeleteItemStockOpname" '{"appVersion": "202604", "modulCode": "invDeleteItemStockOpname", "additionalBody": {"id": "1"}}'

test_api "Save Item Stock Opname" "invSaveItemStockOpname" '{"appVersion": "202604", "modulCode": "invSaveItemStockOpname", "additionalBody": {"itemId": "1", "quantity": 100}}'

# ================== GENSET ==================
echo "=========================================="
echo "SECTION 4: GENSET"
echo "=========================================="

test_api "Get Genset" "getGenset" '{"appVersion": "202604", "modulCode": "getGenset", "additionalBody": {}}'

test_api "Save Genset Available" "saveGensetAvailable" '{"appVersion": "202604", "modulCode": "saveGensetAvailable", "additionalBody": {"id": "1", "available": "true"}}'

test_api "Save Genset Lokasi" "saveGensetLokasi" '{"appVersion": "202604", "modulCode": "saveGensetLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}'

test_api "Save NFC Genset" "saveNfcGenset" '{"appVersion": "202604", "modulCode": "saveNfcGenset", "additionalBody": {"id": "1", "nfc": "NFC001", "gensetNo": "GS001"}}'

# ================== SASIS ==================
echo "=========================================="
echo "SECTION 5: SASIS"
echo "=========================================="

test_api "Get Sasis" "getSasis" '{"appVersion": "202604", "modulCode": "getSasis", "additionalBody": {}}'

test_api "Save Sasis Available" "saveSasisAvailable" '{"appVersion": "202604", "modulCode": "saveSasisAvailable", "additionalBody": {"id": "1", "available": "true"}}'

test_api "Save Sasis Lokasi" "saveSasisLokasi" '{"appVersion": "202604", "modulCode": "saveSasisLokasi", "additionalBody": {"id": "1", "lokasi": "Jakarta"}}'

test_api "Save NFC Sasis" "saveNfcSasis" '{"appVersion": "202604", "modulCode": "saveNfcSasis", "additionalBody": {"id": "1", "nfc": "NFC001", "sasisNo": "SS001"}}'

# ================== ASSET ==================
echo "=========================================="
echo "SECTION 6: ASSET"
echo "=========================================="

test_api "Get Asset" "getAsset" '{"appVersion": "202604", "modulCode": "getAsset", "additionalBody": {}}'

test_api "Save NFC Asset" "saveNfcAsset" '{"appVersion": "202604", "modulCode": "saveNfcAsset", "additionalBody": {"id": "1", "nfc": "NFC001", "assetName": "Asset 01"}}'

# ================== DRIVER ==================
echo "=========================================="
echo "SECTION 7: DRIVER"
echo "=========================================="

test_api "Get Driver" "getDriver" '{"appVersion": "202604", "modulCode": "getDriver", "additionalBody": {}}'

test_api "Save Driver Enabled" "saveDriverEnabled" '{"appVersion": "202604", "modulCode": "saveDriverEnabled", "additionalBody": {"id": 1, "enabled": true}}'

test_api "Save Driver Status" "saveDriverStatus" '{"appVersion": "202604", "modulCode": "saveDriverStatus", "additionalBody": {"id": 1, "status": "active"}}'

test_api "Get Driver Name" "getDriverName" '{"appVersion": "202604", "modulCode": "getDriverName", "additionalBody": {}}'

# ================== DRIVER ORDER ==================
echo "=========================================="
echo "SECTION 8: DRIVER ORDER"
echo "=========================================="

test_api "Get Driver Job" "toGetDriverJob" '{"appVersion": "202604", "modulCode": "toGetDriverJob", "additionalBody": {}}'

test_api "Save Driver Job Truck Plat No" "toSaveDriverJobTruckPlatNo" '{"appVersion": "202604", "modulCode": "toSaveDriverJobTruckPlatNo", "additionalBody": {"id": "1", "platNo": "B 1234 ABC"}}'

test_api "Save Driver Job Sasis No" "toSaveDriverJobSasisNo" '{"appVersion": "202604", "modulCode": "toSaveDriverJobSasisNo", "additionalBody": {"id": "1", "sasisNo": "SS001"}}'

test_api "Save Driver Job Genset No" "toSaveDriverJobGensetNo" '{"appVersion": "202604", "modulCode": "toSaveDriverJobGensetNo", "additionalBody": {"id": "1", "gensetNo": "GS001"}}'

test_api "Save Driver Job" "toSaveDriverJob" '{"appVersion": "202604", "modulCode": "toSaveDriverJob", "additionalBody": {"id": "1", "driverId": "1"}}'

# ================== ADMIN TRUCK ==================
echo "=========================================="
echo "SECTION 9: ADMIN TRUCK"
echo "=========================================="

test_api "Save Driver (Dalam)" "toSaveDriver" '{"appVersion": "202604", "modulCode": "toSaveDriver", "additionalBody": {"id": "1", "driverId": "1"}}'

test_api "Save Trx Type" "toSaveTrxType" '{"appVersion": "202604", "modulCode": "toSaveTrxType", "additionalBody": {"id": "1", "trxType": "IN"}}'

test_api "Save Driver Luar" "toSaveDriverLuar" '{"appVersion": "202604", "modulCode": "toSaveDriverLuar", "additionalBody": {"id": "1", "driverId": "1"}}'

# ================== POM ==================
echo "=========================================="
echo "SECTION 10: POM"
echo "=========================================="

test_api "Get POM" "getPom" '{"appVersion": "202604", "modulCode": "getPom", "additionalBody": {}}'

test_api "Save POM Enabled" "savePomEnabled" '{"appVersion": "202604", "modulCode": "savePomEnabled", "additionalBody": {"id": "1", "enabled": true}}'

test_api "Reset Pump NFC" "resetPumpNfc" '{"appVersion": "202604", "modulCode": "resetPumpNfc", "additionalBody": {"id": "1"}}'

test_api "Save NFC POM" "saveNfcPom" '{"appVersion": "202604", "modulCode": "saveNfcPom", "additionalBody": {"id": "1", "nfc": "NFC001", "machineName": "POM 01"}}'

test_api "NFC Check Mesin" "NfcCheckMesin" '{"appVersion": "202604", "modulCode": "NfcCheckMesin", "additionalBody": {"idmesin": "MESIN001"}}'

test_api "Save POM Stock" "savePomStock" '{"appVersion": "202604", "modulCode": "savePomStock", "additionalBody": {"id": "1", "stock": 100}}'

# ================== BS ==================
echo "=========================================="
echo "SECTION 11: BS (Pelindo)"
echo "=========================================="

test_api "BS Check User" "bsCheckUser" '{"appVersion": "202604", "modulCode": "bsCheckUser", "additionalBody": {}}'

test_api "BS Get Verify" "bsGetVerify" '{"appVersion": "202604", "modulCode": "bsGetVerify", "additionalBody": {}}'

test_api "BS Get Done" "bsGetDone" '{"appVersion": "202604", "modulCode": "bsGetDone", "additionalBody": {}}'

test_api "BS Save Pass" "bsSavePass" '{"appVersion": "202604", "modulCode": "bsSavePass", "additionalBody": {"password": "password123"}}'

test_api "BS Get Snituser" "bsGetSnituser" '{"appVersion": "202604", "modulCode": "bsGetSnituser", "additionalBody": {}}'

test_api "BS Get Pass" "bsGetPass" '{"appVersion": "202604", "modulCode": "bsGetPass", "additionalBody": {}}'

test_api "BS Get Approval" "bsGetApproval" '{"appVersion": "202604", "modulCode": "bsGetApproval", "additionalBody": {}}'

test_api "BS Save Approval" "bsSaveApproval" '{"appVersion": "202604", "modulCode": "bsSaveApproval", "additionalBody": {"id": "1", "approval": "approved"}}'

test_api "BS Get Repo Approval" "bsGetRepoApproval" '{"appVersion": "202604", "modulCode": "bsGetRepoApproval", "additionalBody": {}}'

test_api "BS Get JO" "bsGetJO" '{"appVersion": "202604", "modulCode": "bsGetJO", "additionalBody": {"jo": "JO001"}}'

test_api "BS Get Amount" "bsGetAmount" '{"appVersion": "202604", "modulCode": "bsGetAmount", "additionalBody": {"jo": "JO001", "jenis": "EXPORT"}}'

test_api "BS Get Vessel" "bsGetVessel" '{"appVersion": "202604", "modulCode": "bsGetVessel", "additionalBody": {}}'

test_api "BS Get Real" "bsGetReal" '{"appVersion": "202604", "modulCode": "bsGetReal", "additionalBody": {"jo": "JO001", "vessel": "VES01"}}'

test_api "BS Get TO" "bsGetTO" '{"appVersion": "202604", "modulCode": "bsGetTO", "additionalBody": {"jo": "JO001", "jenis": "EXPORT", "realisasi": "REAL01"}}'

test_api "BS Get Depo Luar" "bsGetDepoLuar" '{"appVersion": "202604", "modulCode": "bsGetDepoLuar", "additionalBody": {}}'

# ================== AP ==================
echo "=========================================="
echo "SECTION 12: AP"
echo "=========================================="

test_api "AP Check User" "apCheckUser" '{"appVersion": "202604", "modulCode": "apCheckUser", "additionalBody": {}}'

test_api "AP Get Vendor" "apGetVendor" '{"appVersion": "202604", "modulCode": "apGetVendor", "additionalBody": {"jenis": "VENDOR"}}'

test_api "AP Get Data" "apGetData" '{"appVersion": "202604", "modulCode": "apGetData", "additionalBody": {"jo": "JO001", "jenis": "IMPORT"}}'

test_api "AP Get JO" "apGetJO" '{"appVersion": "202604", "modulCode": "apGetJO", "additionalBody": {"jo": "JO001"}}'

# ================== DASHBOARD ==================
echo "=========================================="
echo "SECTION 13: DASHBOARD"
echo "=========================================="

test_api "Dashboard Check User" "dashboardCheckUser" '{"appVersion": "202604", "modulCode": "dashboardCheckUser", "additionalBody": {}}'

test_api "Dashboard IN" "dashboardIN" '{"appVersion": "202604", "modulCode": "dashboardIN", "additionalBody": {"lokasi": "Jakarta"}}'

test_api "Dashboard Stripping" "dashboardStripping" '{"appVersion": "202604", "modulCode": "dashboardStripping", "additionalBody": {"lokasi": "Jakarta"}}'

test_api "Dashboard Stuffing" "dashboardStuffing" '{"appVersion": "202604", "modulCode": "dashboardStuffing", "additionalBody": {"lokasi": "Jakarta"}}'

test_api "Dashboard Stripping Update" "dashboardStrippingUpdate" '{"appVersion": "202604", "modulCode": "dashboardStrippingUpdate", "additionalBody": {"id": "1", "status": "done", "containerNo": "CONT001"}}'

test_api "Dashboard Stuffing Update" "dashboardStuffingUpdate" '{"appVersion": "202604", "modulCode": "dashboardStuffingUpdate", "additionalBody": {"id": "1", "status": "done", "containerNo": "CONT001"}}'

# ================== SALES ==================
echo "=========================================="
echo "SECTION 14: SALES"
echo "=========================================="

test_api "Get Sales" "getSales" '{"appVersion": "202604", "modulCode": "getSales", "additionalBody": {}}'

test_api "Get Customer" "getCustomer" '{"appVersion": "202604", "modulCode": "getCustomer", "additionalBody": {"sales": "SALES01"}}'

test_api "Save Customer Blacklist" "saveCustomerBlacklist" '{"appVersion": "202604", "modulCode": "saveCustomerBlacklist", "additionalBody": {"customerId": "1", "status": "blacklist"}}'

# ================== PANTRY ==================
echo "=========================================="
echo "SECTION 15: PANTRY"
echo "=========================================="

test_api "Pantry Get Saldo" "pantryGetSaldo" '{"appVersion": "202604", "modulCode": "pantryGetSaldo", "additionalBody": {}}'

test_api "Pantry Get Order" "pantryGetOrder" '{"appVersion": "202604", "modulCode": "pantryGetOrder", "additionalBody": {}}'

test_api "Pantry Save Order" "pantrySaveOrder" '{"appVersion": "202604", "modulCode": "pantrySaveOrder", "additionalBody": {"orderData": {"items": [], "total": 0}}}'

test_api "Pantry Cancel Order" "pantryCancelOrder" '{"appVersion": "202604", "modulCode": "pantryCancelOrder", "additionalBody": {"orderId": "1"}}'

# ================== PATROL ==================
echo "=========================================="
echo "SECTION 16: PATROL"
echo "=========================================="

test_api "Patrol Get Data" "patrolGetData" '{"appVersion": "202604", "modulCode": "patrolGetData", "additionalBody": {}}'

test_api "Patrol Complete Task" "patrolCompleteTask" '{"appVersion": "202604", "modulCode": "patrolCompleteTask", "additionalBody": {"taskId": "1", "completedAt": "2026-05-05T10:00:00Z"}}'

# ================== POM USER ==================
echo "=========================================="
echo "SECTION 17: POM USER"
echo "=========================================="

test_api "POM Get Pom Log" "pomGetPomLog" '{"appVersion": "202604", "modulCode": "pomGetPomLog", "additionalBody": {"doctype": "POM_OUT"}}'

test_api "POM Get Pom Log New" "pomGetPomLogNew" '{"appVersion": "202604", "modulCode": "pomGetPomLogNew", "additionalBody": {"doctype": "POM_OUT"}}'

test_api "POM Save Pom Log" "pomSavePomLog" '{"appVersion": "202604", "modulCode": "pomSavePomLog", "additionalBody": {"id": "1", "qty": "10", "keterangan": "Test"}}'

test_api "POM Save Pom Log Done" "pomSavePomLogDone" '{"appVersion": "202604", "modulCode": "pomSavePomLogDone", "additionalBody": {"id": "1"}}'

test_api "POM Start Request" "pomStartRequest" '{"appVersion": "202604", "modulCode": "pomStartRequest", "additionalBody": {"pomId": "1", "qty": "10"}}'

# ================== ACCIDENT ==================
echo "=========================================="
echo "SECTION 18: ACCIDENT"
echo "=========================================="

test_api "TA Get Accident" "taGetAccident" '{"appVersion": "202604", "modulCode": "taGetAccident", "additionalBody": {"accidentType": "TRUCK"}}'

test_api "TA Approval Accident" "taApprovalAccident" '{"appVersion": "202604", "modulCode": "taApprovalAccident", "additionalBody": {"id": "1", "action": "approve"}}'

test_api "TA Delete Accident" "taDeleteAccident" '{"appVersion": "202604", "modulCode": "taDeleteAccident", "additionalBody": {"id": "1"}}'

test_api "TA Request Approval Accident" "taRequestApprovalAccident" '{"appVersion": "202604", "modulCode": "taRequestApprovalAccident", "additionalBody": {"id": "1"}}'

test_api "Get Accident" "toGetAccident" '{"appVersion": "202604", "modulCode": "toGetAccident", "additionalBody": {}}'

test_api "Approve Accident" "toApproveAccident" '{"appVersion": "202604", "modulCode": "toApproveAccident", "additionalBody": {"id": "1", "approval": "approved"}}'

test_api "Get Container" "getContainer" '{"appVersion": "202604", "modulCode": "getContainer", "additionalBody": {}}'

# ================== SECURITY GATE ==================
echo "=========================================="
echo "SECTION 19: SECURITY GATE"
echo "=========================================="

test_api "SG Get Gate Log" "sgGetGateLog" '{"appVersion": "202604", "modulCode": "sgGetGateLog", "additionalBody": {}}'

test_api "SG Get TO" "sgGetTO" '{"appVersion": "202604", "modulCode": "sgGetTO", "additionalBody": {}}'

# ================== VESSEL ==================
echo "=========================================="
echo "SECTION 20: VESSEL"
echo "=========================================="

test_api "Get Vessel Name" "getVesselName" '{"appVersion": "202604", "modulCode": "getVesselName", "additionalBody": {}}'

test_api "Get Vessel Schedule" "getVesselSchedule" '{"appVersion": "202604", "modulCode": "getVesselSchedule", "additionalBody": {"port": "Jakarta", "eta": "2026-05-10"}}'

test_api "Get Port Origin" "getPortOrigin" '{"appVersion": "202604", "modulCode": "getPortOrigin", "additionalBody": {"vessel": "VES01"}}'

test_api "Get Port Destination" "getPortDestination" '{"appVersion": "202604", "modulCode": "getPortDestination", "additionalBody": {"vessel": "VES01"}}'

# ================== SIMULATE ==================
echo "=========================================="
echo "SECTION 21: SIMULATE"
echo "=========================================="

test_api "BS Simulasi Get JO" "bsSimulasiGetJO" '{"appVersion": "202604", "modulCode": "bsSimulasiGetJO", "additionalBody": {"jo": "JO001"}}'

test_api "BS Simulasi Get Amount" "bsSimulasiGetAmount" '{"appVersion": "202604", "modulCode": "bsSimulasiGetAmount", "additionalBody": {"jo": "JO001", "jenis": "EXPORT"}}'

# ================== PLUG ==================
echo "=========================================="
echo "SECTION 22: PLUG"
echo "=========================================="

test_api "Plug Get Plug Log" "plugGetPlugLog" '{"appVersion": "202604", "modulCode": "plugGetPlugLog", "additionalBody": {"doctype": "OUT"}}'

test_api "Plug Save Plug Log" "plugSavePlugLog" '{"appVersion": "202604", "modulCode": "plugSavePlugLog", "additionalBody": {"id": "1", "qty": "10"}}'

test_api "Check Plug JO" "checkPlugJo" '{"appVersion": "202604", "modulCode": "checkPlugJo", "additionalBody": {"docNo": "DOC001"}}'

# ================== LIFECYCLE ==================
echo "=========================================="
echo "SECTION 23: LIFECYCLE"
echo "=========================================="

test_api "Save User Heartbeat" "saveUserHeartbeat" '{"appVersion": "202604", "modulCode": "saveUserHeartbeat", "additionalBody": {"lat": "-6.200000", "lng": "106.816666", "accuracy": "10.0"}}'

test_api "Kill Heartbeat" "killHeartbeat" '{"appVersion": "202604", "modulCode": "killHeartbeat", "additionalBody": {"imei": "123456789012345"}}'

# ================== CHECK NFC ==================
echo "=========================================="
echo "SECTION 24: CHECK NFC"
echo "=========================================="

test_api "Check NFC" "checkNfc" '{"appVersion": "202604", "modulCode": "checkNfc", "additionalBody": {"nfc": "NFC001"}}'

echo "=========================================="
echo "Test Complete!"
echo "=========================================="