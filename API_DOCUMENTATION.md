# TriDominic Complete API Documentation (v202603)

---

## A. callApiFetch (165 instances)

| No | File | Line | Function | modulCode | Parameters | Data Type |
|----|------|------|----------|-----------|------------|-----------|
| **TRUCK** |||||||
| 1 | lib/controller/trucklist_c.dart | 63 | `fetchTrucks(BuildContext context)` | `getTruck` | - | - |
| 2 | lib/controller/trucklist_c.dart | 84 | `resetNfc(String truckId)` | `resetNfc` | `id` | `String` |
| 3 | lib/controller/trucklist_c.dart | 105 | `changeTruck(String truckId, String set)` | `saveTruckAvailable` | `id`, `available` | `String`, `String` |
| 4 | lib/controller/trucklist_c.dart | 130 | `fetchLocations()` | `getLokasi` | - | - |
| 5 | lib/controller/trucklist_c.dart | 154 | `changeLocation(String truckId, String lokasi)` | `saveTruckLokasi` | `id`, `lokasi` | `String`, `String` |
| 6 | lib/controller/trucklist_c.dart | 297 | `sendNFCTags(String nfctags, String truckId, String platNo)` | `saveNfcTruck` | `id`, `nfc`, `platNo` | `String`, `String`, `String` |
| **INVENTORY** |||||||
| 7 | lib/controller/inventorylist_c.dart | 92 | `fetchInventory(BuildContext context)` | `invGetItemStockOpname` | - | - |
| 8 | lib/controller/inventorylist_c.dart | 115 | `resetNfc(String inventoryId)` | `resetNfc` | `id` | `String` |
| 9 | lib/controller/inventorylist_c.dart | 137 | `changeInventory(String inventoryId, String set)` | `saveInventoryAvailable` | `id`, `available` | `String`, `String` |
| 10 | lib/controller/inventorylist_c.dart | 162 | `fetchLocations()` | `getLokasi` | - | - |
| 11 | lib/controller/inventorylist_c.dart | 183 | `changeLocation(String inventoryId, String lokasi)` | `saveInventoryLokasi` | `id`, `lokasi` | `String`, `String` |
| 12 | lib/controller/inventorylist_c.dart | 311 | `sendNFCTags(String nfctags, String inventoryId, String inventoryNo)` | `saveNfcInventory` | `id`, `nfc`, `inventoryNo` | `String`, `String`, `String` |
| 13 | lib/controller/inventorylist_c.dart | 366 | `deleteInventory(String id, BuildContext context)` | `invDeleteItemStockOpname` | `id` | `String` |
| **INVENTORY DETAIL** |||||||
| 14 | lib/controller/inventory_detail_controller.dart | 18 | `fetchSites()` | `invGetSite` | - | - |
| 15 | lib/controller/inventory_detail_controller.dart | 28 | `fetchItems()` | `invGetItem` | - | - |
| 16 | lib/controller/inventory_detail_controller.dart | 48 | `saveStockOpname(dynamic body)` | `invSaveItemStockOpname` | `body` | `Map<String, dynamic>` |
| **GENSET** |||||||
| 17 | lib/controller/gensetlist_c.dart | 63 | `fetchGensets(BuildContext context)` | `getGenset` | - | - |
| 18 | lib/controller/gensetlist_c.dart | 84 | `resetNfc(String gensetId)` | `resetNfc` | `id` | `String` |
| 19 | lib/controller/gensetlist_c.dart | 105 | `changeGenset(String gensetId, String set)` | `saveGensetAvailable` | `id`, `available` | `String`, `String` |
| 20 | lib/controller/gensetlist_c.dart | 129 | `fetchLocations()` | `getLokasi` | - | - |
| 21 | lib/controller/gensetlist_c.dart | 150 | `changeLocation(String gensetId, String lokasi)` | `saveGensetLokasi` | `id`, `lokasi` | `String`, `String` |
| 22 | lib/controller/gensetlist_c.dart | 276 | `sendNFCTags(String nfctags, String gensetId, String gensetNo)` | `saveNfcGenset` | `id`, `nfc`, `gensetNo` | `String`, `String`, `String` |
| **SASIS** |||||||
| 23 | lib/controller/sasislist_c.dart | 63 | `fetchSasis(BuildContext context)` | `getSasis` | - | - |
| 24 | lib/controller/sasislist_c.dart | 84 | `resetNfc(String sasisId)` | `resetNfc` | `id` | `String` |
| 25 | lib/controller/sasislist_c.dart | 105 | `changeSasis(String sasisId, String set)` | `saveSasisAvailable` | `id`, `available` | `String`, `String` |
| 26 | lib/controller/sasislist_c.dart | 129 | `fetchLocations()` | `getLokasi` | - | - |
| 27 | lib/controller/sasislist_c.dart | 150 | `changeLocation(String sasisId, String lokasi)` | `saveSasisLokasi` | `id`, `lokasi` | `String`, `String` |
| 28 | lib/controller/sasislist_c.dart | 276 | `sendNFCTags(String nfctags, String sasisId, String sasisNo)` | `saveNfcSasis` | `id`, `nfc`, `sasisNo` | `String`, `String`, `String` |
| **ASSET** |||||||
| 29 | lib/controller/assetlist_c.dart | 77 | `fetchAssets(BuildContext context)` | `getAsset` | - | - |
| 30 | lib/controller/assetlist_c.dart | 190 | `_sendNFCTags(String nfctags, String assetId, String assetName)` | `saveNfcAsset` | `id`, `nfc`, `assetName` | `String`, `String`, `String` |
| **DRIVER** |||||||
| 31 | lib/controller/driver_list_controller.dart | 10 | `fetchDrivers()` | `getDriver` | - | - |
| 32 | lib/controller/driver_list_controller.dart | 33 | `setDriverEnabled(int driverId, bool enabled)` | `saveDriverEnabled` | `id`, `enabled` | `int`, `bool` |
| 33 | lib/controller/driver_list_controller.dart | 55 | `setDriverStatus(int driverId, String status)` | `saveDriverStatus` | `id`, `status` | `int`, `String` |
| **DRIVER ORDER** |||||||
| 34 | lib/controller/driver_order_controller.dart | 26 | `fetchOrders()` | `toGetDriverJob` | - | - |
| 35 | lib/controller/driver_order_controller.dart | 179 | `nfcplatno(String id, String rfid)` | `toSaveDriverJobTruckPlatNo` | `id`, `platNo` | `String`, `String` |
| 36 | lib/controller/driver_order_controller.dart | 203 | `nfcsasisno(String id, String rfid)` | `toSaveDriverJobSasisNo` | `id`, `sasisNo` | `String`, `String` |
| 37 | lib/controller/driver_order_controller.dart | 227 | `nfcgensetno(String id, String rfid)` | `toSaveDriverJobGensetNo` | `id`, `gensetNo` | `String`, `String` |
| **ADMIN TRUCK DALAM** |||||||
| 38 | lib/controller/admin_truck_dalam_controller.dart | 30 | `callapifetch(String modulcode)` | Dynamic | - | - |
| 39 | lib/controller/admin_truck_dalam_controller.dart | 235 | `updateDriver(String toId, [String? driverId])` | `toSaveDriver` | `id`, `driverId` | `String`, `String?` |
| 40 | lib/controller/admin_truck_dalam_controller.dart | 244 | `cancelTO(String toId, String trxType)` | `toSaveTrxType` | `id`, `trxType` | `String`, `String` |
| **ADMIN TRUCK LUAR** |||||||
| 41 | lib/controller/admin_truck_luar_controller.dart | 30 | `callapifetch(String modulcode)` | Dynamic | - | - |
| 42 | lib/controller/admin_truck_luar_controller.dart | 230 | `updateDriverLuar(String toId, [String? driverId])` | `toSaveDriverLuar` | `id`, `driverId` | `String`, `String?` |
| 43 | lib/controller/admin_truck_luar_controller.dart | 239 | `moveToInside(String toId, String trxType)` | `toSaveTrxType` | `id`, `trxType` | `String`, `String` |
| **USER** |||||||
| 44 | lib/controller/userlistpage_c.dart | 43 | `toggleBs(String userId, String currentBs)` | `saveUserBs` | `userId`, `bs` | `String`, `String` |
| 45 | lib/controller/userlistpage_c.dart | 84 | `fetchUsers(BuildContext context)` | `getSnituser` | - | - |
| 46 | lib/controller/userlistpage_c.dart | 105 | `resetImei(String userId)` | `resetImei` | `id` | `String` |
| 47 | lib/controller/userlistpage_c.dart | 126 | `resetPassword(String userId)` | `resetPassword` | `id` | `String` |
| 48 | lib/controller/userlistpage_c.dart | 147 | `changeUser(String userId, String set)` | `saveUserEnabled` | `id`, `enabled` | `String`, `String` |
| 49 | lib/controller/userlistpage_c.dart | 172 | `fetchLocations()` | `getLokasi` | - | - |
| 50 | lib/controller/userlistpage_c.dart | 195 | `changeLocation(String userId, String lokasi)` | `saveSnituserLokasi` | `id`, `lokasi` | `String`, `String` |
| 51 | lib/controller/userlistpage_c.dart | 222 | `enableBs(String userId)` | `enableBs` | `id`, `bs` | `String`, `String` |
| **POM** |||||||
| 52 | lib/controller/pump_machine_master_c.dart | 63 | `fetchMachines(BuildContext context)` | `getPom` | - | - |
| 53 | lib/controller/pump_machine_master_c.dart | 85 | `changeEnable(String machineId, String set)` | `savePomEnabled` | `id`, `enabled` | `String`, `bool` |
| 54 | lib/controller/pump_machine_master_c.dart | 107 | `resetNfc(String machineId)` | `resetPumpNfc` | `id` | `String` |
| 55 | lib/controller/pump_machine_master_c.dart | 226 | `_sendNfcToServer(String nfctags, String machineId, String machineName)` | `saveNfcPom` | `id`, `nfc`, `machineName` | `String`, `String`, `String` |
| **BS CONTROLLER** |||||||
| 56 | lib/controller/bs_controller.dart | 45 | `onInit()` | `bsCheckUser` | - | - |
| 57 | lib/controller/besverify_c.dart | 107 | `fetchUsers()` | `bsGetVerify` | - | - |
| 58 | lib/controller/bs_done_controller.dart | 59 | `fetchList()` | `bsGetDone` | - | - |
| 59 | lib/controller/bsbypass_c.dart | 75 | `bypassUser(String userId)` | `bsSavePass` | `password` | `String` |
| 60 | lib/controller/bsbypass_c.dart | 106 | `changeUser(String userId, String set)` | `saveUserEnabled` | `id`, `enabled` | `String`, `String` |
| 61 | lib/controller/bsbypass_c.dart | 138 | `fetchUsers()` | `bsGetSnituser` | - | - |
| 62 | lib/controller/bsbypass_c.dart | 160 | `fetchUsersBS()` | `bsGetPass` | - | - |
| 63 | lib/controller/processbspj_controller.dart | 13 | `fetchItems()` | `bsGetApproval` | - | - |
| 64 | lib/controller/processbspj_controller.dart | 36 | `saveApproval(String id)` | `bsSaveApproval` | `id`, `approval` | `String`, `String` |
| 65 | lib/controller/processbspj_controller.dart | 58 | `saveApproval(String id)` | `bsSaveApproval` | `id` | `String` |
| 66 | lib/controller/repobs_controller.dart | 17 | `fetchItems()` | `bsGetRepoApproval` | - | - |
| **DASHBOARD** |||||||
| 67 | lib/controller/dashboard_location_controller.dart | 16 | `fetchLocations()` | `dashboardCheckUser` | - | - |
| 68 | lib/controller/dashboard_destination_controller.dart | 70 | `onInit()` | `dashboardIN` | `lokasi` | `String` |
| 69 | lib/controller/dashboard_stripping_controller.dart | 56 | `fetchData()` | `dashboardStripping` | `lokasi` | `String?` |
| 70 | lib/controller/dashboard_stuffing_controller.dart | 56 | `fetchData()` | `dashboardStuffing` | `lokasi` | `String?` |
| **PANTRY** |||||||
| 71 | lib/controller/pantry_controller.dart | 298 | `saveOrder(Map<String, dynamic> orderData)` | `pantrySaveOrder` | `orderData` | `Map<String, dynamic>` |
| 72 | lib/controller/pantry_controller.dart | 389 | `cancelOrder(String orderId)` | `pantryCancelOrder` | `orderId` | `String` |
| **PATROL** |||||||
| 73 | lib/controller/patrol_controller.dart | 43 | `fetchData()` | `patrolGetData` | - | - |
| 74 | lib/controller/patrol_controller.dart | 203 | `completeTask(String taskId, DateTime completedAt)` | `patrolCompleteTask` | `taskId`, `completedAt` | `String`, `String` |
| **HIKVISION** |||||||
| 75 | lib/controller/hikvision_controller.dart | 128 | `createUser(Map<String, dynamic> userData)` | `createHikvisionUserRequest` | `userData` | `Map<String, dynamic>` |
| 76 | lib/controller/hikvision_controller.dart | 173 | `updateUser(Map<String, dynamic> userData)` | `updateHikvisionUserRequest` | `userData` | `Map<String, dynamic>` |
| 77 | lib/controller/hikvision_controller.dart | 218 | `deleteUser(String userId)` | `deleteHikvisionUserRequest` | `id` | `String` |
| 78 | lib/controller/hikvision_controller.dart | 271 | `openDoor(String deviceId)` | `hikvisionDeviceOpenRequest` | `deviceId` | `String` |
| 79 | lib/controller/hikvision_controller.dart | 312 | (various) | `hikvisionPersonSetStatusRequest` | - | - |
| **SALES** |||||||
| 80 | lib/controller/sales_customer_c.dart | 90 | `fetchCustomer(String salescode)` | `getCustomer` | `sales` | `String` |
| 81 | lib/controller/salescustomer_c.dart | 90 | `fetchCustomer()` | `getCustomer` | `sales` | `String` |
| **VIEW - POM** |||||||
| 82 | lib/view/pom/refil_user.dart | 52 | `checkMesin(String scannedId)` | `NfcCheckMesin` | `idmesin` | `String` |
| 83 | lib/view/pom/refil_user.dart | 76 | `updateStok(dynamic id, dynamic stok)` | `savePomStock` | `id`, `stock` | `dynamic`, `dynamic` |
| 84 | lib/view/pom/refilpom.dart | 47 | `updateStok(dynamic id, dynamic stok)` | `savePomStock` | `id`, `stock` | `dynamic`, `dynamic` |
| **VIEW - POM USER** |||||||
| 85 | lib/view/pomuser/menu.dart | 78 | `fetchPomLog()` | `pomGetPomLog` | `doctype` | `String` |
| 86 | lib/view/pomuser/menu.dart | 114 | `fetchPomHistory()` | `pomGetPomLog` | `doctype` | `String` |
| 87 | lib/view/pomuser/menu.dart | 139 | `fetchPomLogNew()` | `pomGetPomLogNew` | `doctype` | `String` |
| 88 | lib/view/pomuser/menu.dart | 213 | `savePomLogDone()` | `pomSavePomLogDone` | `id` | `String?` |
| 89 | lib/view/pomuser/menu.dart | 281 | `savePomLog(BuildContext context)` | `pomSavePomLog` | `id`, `qty`, `keterangan` | `String`, `String`, `String` |
| 90 | lib/view/pomuser/menu.dart | 503 | `fetchGensetLog()` | `pomGetPomLog` | `doctype` | `String` |
| 91 | lib/view/pomuser/menu.dart | 535 | `fetchGensetHistory()` | `pomGetPomLog` | `doctype` | `String` |
| 92 | lib/view/pomuser/menu.dart | 588 | `startRequest()` | `pomStartRequest` | `pomId`, `qty` | `String`, `String` |
| 93 | lib/view/pomuser/menu.dart | 732 | `saveGensetLog(BuildContext context)` | `pomSavePomLog` | `id`, `qty`, `keterangan` | `String`, `String`, `String` |
| **VIEW - BS** |||||||
| 94 | lib/view/bs/pilihjo.dart | 323 | `loadJo()` | `bsGetJO` | `body` | `Map<String, dynamic>` |
| 95 | lib/view/bs/hasilbs.dart | 80 | `fetchBonSementaraData(String joList)` | `bsGetAmount` | `jo`, `jenis` | `String`, `String` |
| 96 | lib/view/bs/pilihkapal.dart | 294 | `loadVessel()` | `bsGetVessel` | - | - |
| 97 | lib/view/bs/pilihrealisasi.dart | 360 | `loadRealisasi()` | `bsGetReal` | `jo`, `vessel` | `String`, `String` |
| 98 | lib/view/bs/pilihto.dart | 459 | `loadTo()` | `bsGetTO` | `jo`, `jenis`, `realisasi` | `String`, `String`, `String` |
| 99 | lib/view/bs/prosespelindo.dart | 80 | `fetchVendorOptions()` | `bsGetDepoLuar` | - | - |
| 100 | lib/view/bs/prosespelindo.dart | 93 | `fetchBonSementaraData()` | `bsGetAmount` | - | - |
| 101 | lib/view/bs/tipe-bs.dart | 39 | `getUserStatus()` | `bsCheckUser` | - | - |
| **VIEW - AP** |||||||
| 102 | lib/view/ap/location-ap.dart | 31 | `getLocationData()` | `apCheckUser` | - | - |
| 103 | lib/view/ap/pilihjo-ap.dart | 270 | `loadJo()` | `apGetJO` | `body` | `Map<String, dynamic>` |
| 104 | lib/view/ap/pilihdata-ap.dart | 606 | `loadData()` | `apGetData` | `jo`, `jenis` | `String`, `String` |
| 105 | lib/view/ap/pilihvendor-ap.dart | 318 | `loadVendor()` | `apGetVendor` | `jenis` | `String` |
| 106 | lib/view/ap/pilihto-ap.dart | 248 | `loadTo()` | `apGetData` | `body` | `Map<String, dynamic>` |
| 107 | lib/view/ap/pilihkapal-ap.dart | 241 | `loadKapal()` | `apGetData` | `jo`, `jenis` | `String`, `String` |
| 108 | lib/view/ap/hasilap.dart | 217 | `loadVendor()` | `apGetVendor` | `jenis`, `additionalBody` | `String`, `Map<String, dynamic>` |
| **VIEW - ACCIDENT** |||||||
| 109 | lib/view/accident_list.dart | 193 | `fetchAccidents()` | `taGetAccident` | `accidentType` | `String` |
| 110 | lib/view/accident_list.dart | 306 | `approve(...)` | `taApprovalAccident` | `id`, `action` | `String`, `String` |
| 111 | lib/view/accident_list.dart | 383 | `delete(...)` | `taDeleteAccident` | `id` | `String` |
| 112 | lib/view/accident_list.dart | 434 | `delete(...)` | `taDeleteAccident` | `id` | `String` |
| 113 | lib/view/accident_list.dart | 483 | `requestApproval(...)` | `taRequestApprovalAccident` | `id` | `String` |
| 114 | lib/view/accident_container_list.dart | 112 | `fetchAccidents()` | `taGetAccident` | `accidentType` | `String` |
| 115 | lib/view/accident_container_list.dart | 222 | `approve(...)` | `taApprovalAccident` | `id`, `action` | `String`, `String` |
| 116 | lib/view/accident_container_list.dart | 283 | `approve(...)` | `taApprovalAccident` | - | - |
| 117 | lib/view/accident_container_list.dart | 332 | `delete(...)` | `taDeleteAccident` | `id` | `String` |
| 118 | lib/view/accident_container_list.dart | 376 | `requestApproval(...)` | `taRequestApprovalAccident` | `id` | `String` |
| 119 | lib/view/accident_container.dart | 365 | `_pickContainer()` | `getContainer` | - | - |
| 120 | lib/view/accident_approval.dart | 88 | `fetchAll()` | `toGetAccident` | - | - |
| 121 | lib/view/accident_approval.dart | 114 | `approve(Accident a)` | `toApproveAccident` | `id`, `approval` | `String`, `String` |
| 122 | lib/view/accident.dart | 412 | `_pickDriver()` | `getDriverName` | - | - |
| 123 | lib/view/accident.dart | 503 | `_pickTruck()` | `getTruck` | - | - |
| **VIEW - SECURITY** |||||||
| 124 | lib/view/security/form.dart | 64 | `fetchDropdownData()` | `getContainer` | - | - |
| 125 | lib/view/security/form.dart | 295 | `pickDriver(...)` | `getDriverName` | - | - |
| 126 | lib/view/security/form.dart | 387 | `pickTruck(...)` | `getTruck` | - | - |
| 127 | lib/view/security/gatelog.dart | 237 | `fetchGateLogs()` | `sgGetGateLog` | - | - |
| 128 | lib/view/security/print.dart | 15 | `fetchpdf(...)` | `sgGetTO` | - | - |
| 129 | lib/view/security/print.dart | 36 | `printPdf(...)` | Dynamic | `id` | `String` |
| **VIEW - VESSEL** |||||||
| 130 | lib/view/vessel_schedule.dart | 36 | `_fetchVesselNames()` | `getVesselName` | - | - |
| 131 | lib/view/vessel_schedule.dart | 59 | (async) | `getPortOrigin` | `vessel` | `String` |
| 132 | lib/view/vessel_schedule.dart | 64 | (async) | `getPortDestination` | `vessel` | `String` |
| 133 | lib/view/vessel_schedule.dart | 118 | `_fetchSchedule()` | `getVesselSchedule` | `port`, `eta` | `String`, `String` |
| **VIEW - SALES** |||||||
| 134 | lib/view/sales_activity.dart | 69 | `fetchSales()` | `getSales` | - | - |
| 135 | lib/view/salescustomer.dart | 35 | `customerKeychange(String id, String blacklist)` | `saveCustomerBlacklist` | `customerId`, `status` | `String`, `String` |
| **VIEW - PANTRY** |||||||
| 136 | lib/view/pantry/pantry_orders.dart | 40 | `_fetchBalance()` | `pantryGetSaldo` | - | - |
| 137 | lib/view/pantry/pantry_orders.dart | 62 | `_fetchHistory()` | `pantryGetOrder` | - | - |
| 138 | lib/view/pantry/pantry_cart.dart | 389 | `checkout()` | `pantryGetSaldo` | - | - |
| **VIEW - PLUG** |||||||
| 139 | lib/view/plug/menu.dart | 65 | `fetchPlugLog()` | `plugGetPlugLog` | `doctype` | `String` |
| 140 | lib/view/plug/menu.dart | 98 | `savePlugLog(...)` | `plugSavePlugLog` | `id`, `qty` | `String`, `String` |
| 141 | lib/view/plug/menu.dart | 158 | `checkJo(String scanned)` | `checkPlugJo` | `docNo` | `String` |
| **VIEW - SIMULATE** |||||||
| 142 | lib/view/simulate/pilihjo.dart | 367 | `loadJo()` | `bsSimulasiGetJO` | `body` | `Map<String, dynamic>` |
| 143 | lib/view/simulate/pilihjo.dart | 439 | `loadAmount()` | `bsSimulasiGetAmount` | `body` | `Map<String, dynamic>` |
| 144 | lib/view/simulate/simulatebs.dart | 53 | `fetchLokasi()` | `getLokasi` | `statusAdaKantor` | `String` |
| 145 | lib/view/simulate/simulatebs.dart | 69 | `fetchVessel()` | `getVessel` | - | - |
| 146 | lib/view/simulate/prosespelindo.dart | 65 | `fetchVendorOptions()` | `bsGetDepoLuar` | - | - |
| 147 | lib/view/simulate/prosespelindo.dart | 103 | `fetchBonSementaraData()` | `bsSimulasiGetAmount` | - | - |
| 148 | lib/view/simulate/simulatehasilbs.dart | 79 | `_fetchBonSementara()` | `bsSimulasiGetAmount` | - | - |
| **VIEW - DASHBOARD** |||||||
| 149 | lib/view/dashboard_stripping_page.dart | 264 | `updateStatus(...)` | `dashboardStrippingUpdate` | `id`, `status`, `containerNo` | `String`, `String`, `String` |
| 150 | lib/view/dashboard_stuffing_page.dart | 277 | `updateStatus(...)` | `dashboardStuffingUpdate` | `id`, `status`, `containerNo` | `String`, `String`, `String` |
| **VIEW - DRIVER ORDER** |||||||
| 151 | lib/view/driver_order_page.dart | 367 | (dynamic) | Dynamic | - | - |
| 152 | lib/view/driver_order_page.dart | 469 | `saveJob(...)` | `toSaveDriverJob` | - | - |
| **VIEW - OTHERS** |||||||
| 153 | lib/view/widgets/card_layanan.dart | 1023 | `checkNfc(String nfcId)` | `checkNfc` | `nfc` | `String` |
| 154 | lib/view/apiactionbutton.dart | 84 | `fetchUsers()` | `getSnituser` | - | - |
| 155 | lib/view/usermap.dart | 49 | `fetchUsers()` | `getSnituser` | - | - |
| **SERVICES** |||||||
| 156 | lib/services/lifecycle_service.dart | 74 | `_sendHeartbeat()` | `saveUserHeartbeat` | `lat`, `lng`, `accuracy` | `String`, `String`, `double` |
| 157 | lib/services/lifecycle_service.dart | 92 | `_sendLifecyclePing(String status)` | `saveUserHeartbeat` | `lat`, `lng`, `accuracy` | `String`, `String`, `double` |
| 158 | lib/services/lifecycle_service.dart | 113 | `_sendShutdownHeartbeat()` | `killHeartbeat` | `imei` | `String` |

---

## B. Manual HTTP (62 instances)

| No | File | Line | Method | Endpoint/Path | Body Parameters | Data Type |
|----|------|------|--------|---------------|------------------|-----------|
| **CONTROLLER** |||||||
| 1 | lib/controller/login_controller.dart | 109 | POST | `/api/token` | `imei`, `version`, `timezone`, `latitude`, `longitude` | `String`, `String`, `String`, `double?`, `double?` |
| 2 | lib/controller/login_controller.dart | 214 | POST | `apisnit` | `modulCode: saveNfc`, `nfc` | `String`, `String` |
| 3 | lib/controller/driver_manual_absen_controller.dart | 235 | POST | `/api/absensi` | `type`, `imei`, `image`, `lat`, `lng`, `address` | `String`, `String`, `String`, `double`, `double`, `String` |
| 4 | lib/controller/camera_controller.dart | 355 | POST | `/api/absensi` | Absensi data + image (base64) | Various |
| 5 | lib/controller/driver_absen_controller.dart | 355 | POST | `/api/absensi` | Absensi data + image (base64) | Various |
| 6 | lib/controller/manual_camera_controller.dart | 246 | POST | `/api/absensi` | Absensi data + image (base64) | Various |
| 7 | lib/controller/salesplan_controller.dart | 36 | POST | `apisnit` | Sales plan data | `Map<String, dynamic>` |
| 8 | lib/controller/salesplan_controller.dart | 190 | POST | `apisnit` | Sales plan data | `Map<String, dynamic>` |
| 9 | lib/controller/salesplan_controller.dart | 249 | POST | `apisnit` | Sales plan data | `Map<String, dynamic>` |
| 10 | lib/controller/salesplan_controller.dart | 382 | POST | `apisnit` | Sales plan data | `Map<String, dynamic>` |
| 11 | lib/controller/pantry_controller.dart | 94 | GET | Local pantry server | - | - |
| 12 | lib/controller/pantry_controller.dart | 144 | GET | Local pantry server | - | - |
| 13 | lib/controller/driver_map_controller.dart | 34 | GET | Maps API | - | - |
| 14 | lib/controller/driver_map_controller.dart | 71 | GET | Maps API | - | - |
| 15 | lib/controller/registration_controller.dart | 37 | POST | Auth register | Registration data | `Map<String, dynamic>` |
| 16 | lib/controller/registration_controller.dart | 38 | POST | Auth register | Registration data | `Map<String, dynamic>` |
| **VIEW** |||||||
| 17 | lib/view/patroladmin.dart | 82 | GET | Patrol admin API | - | - |
| 18 | lib/view/patroladmin.dart | 95 | GET | Patrol admin API | - | - |
| 19 | lib/view/patroladmin.dart | 112 | POST | Patrol admin API | Patrol data | `Map<String, dynamic>` |
| 20 | lib/view/patroladmin.dart | 161 | DELETE | Patrol admin API | - | - |
| 21 | lib/view/patroladmin.dart | 189 | GET | Patrol admin API | - | - |
| 22 | lib/view/patroladmin.dart | 204 | POST | Patrol admin API | Patrol data | `Map<String, dynamic>` |
| 23 | lib/view/patroladmin.dart | 232 | DELETE | Patrol admin API | - | - |
| 24 | lib/view/accident.dart | 185 | GET | Accident API | - | - |
| 25 | lib/view/accident.dart | 343 | GET | Accident API | - | - |
| 26 | lib/view/accident_container.dart | 186 | GET | Container API | - | - |
| 27 | lib/view/accident_container.dart | 333 | GET | Container API | - | - |
| 28 | lib/view/driver_detail.dart | 124 | GET | Driver API | - | - |
| 29 | lib/view/driver_detail.dart | 171 | GET | Driver API | - | - |
| 30 | lib/view/address_route_page.dart | 29 | GET | Address route | - | - |
| 31 | lib/view/address_route_page.dart | 109 | GET | Address route | - | - |
| 32 | lib/view/sales_customer.dart | 46 | POST | Customer API | Customer data | `Map<String, dynamic>` |
| 33 | lib/view/sales_customer_detail.dart | 66 | POST | Customer detail API | Customer detail | `Map<String, dynamic>` |
| 34 | lib/view/salescustomer_detail.dart | 70 | POST | Customer detail API | Customer detail | `Map<String, dynamic>` |
| 35 | lib/view/inventorylist.dart | 54 | POST | Inventory API | Inventory data | `Map<String, dynamic>` |
| 36 | lib/view/trucklist.dart | 114 | POST | Truck API | Truck data | `Map<String, dynamic>` |
| 37 | lib/view/gensetlist.dart | 107 | POST | Genset API | Genset data | `Map<String, dynamic>` |
| 38 | lib/view/sasislist.dart | 107 | POST | Sasis API | Sasis data | `Map<String, dynamic>` |
| 39 | lib/view/bs/hasilbs.dart | 181 | POST | BS amount API | BS amount data | `Map<String, dynamic>` |
| 40 | lib/view/bs/hasilto.dart | 69 | POST | BS TO API | BS TO data | `Map<String, dynamic>` |
| 41 | lib/view/bs/hasilto.dart | 188 | POST | BS TO API | BS TO data | `Map<String, dynamic>` |
| 42 | lib/view/bs/pilihvendor.dart | 93 | POST | Vendor API | Vendor data | `Map<String, dynamic>` |
| 43 | lib/view/bs/pilihvendor.dart | 194 | POST | Vendor API | Vendor data | `Map<String, dynamic>` |
| 44 | lib/view/bs/pilihvendor.dart | 578 | POST | Vendor API | Vendor data | `Map<String, dynamic>` |
| 45 | lib/view/bs/hasilbs-coc.dart | 71 | POST | BS COC API | BS COC data | `Map<String, dynamic>` |
| 46 | lib/view/bs/hasilbs-coc.dart | 188 | POST | BS COC API | BS COC data | `Map<String, dynamic>` |
| 47 | lib/view/bs/pilih-coc.dart | 300 | POST | BS COC API | BS COC data | `Map<String, dynamic>` |
| 48 | lib/view/bs/pilih-coc-container.dart | 299 | POST | COC container API | COC container | `Map<String, dynamic>` |
| 49 | lib/view/bs/hasilrealisasi.dart | 327 | POST | Realisasi API | Realisasi data | `Map<String, dynamic>` |
| 50 | lib/view/ap/hasilap.dart | 564 | POST | AP API | AP data | `Map<String, dynamic>` |
| 51 | lib/view/pomuser/pommini.dart | 80 | POST | POM API | POM data | `Map<String, dynamic>` |
| 52 | lib/view/simulate/simulatehasilbs.dart | 116 | POST | Simulate API | Simulate data | `Map<String, dynamic>` |
| 53 | lib/view/security/form.dart | 267 | POST (stream) | Form upload API | Form upload | Stream |
| **MAIN** |||||||
| 54 | lib/main.dart | 337 | POST | Notifications API | Notifications | `Map<String, dynamic>` |
| 55 | lib/main.dart | 700 | POST | Update check API | Update check | `Map<String, dynamic>` |
| **SERVICES** |||||||
| 56 | lib/services/background_service.dart | 353 | POST | Heartbeat API | Heartbeat | `Map<String, dynamic>` |

---

## Summary

| Category | Count |
|----------|-------|
| **Total callApiFetch** | 158 instances |
| **Total Manual HTTP** | 56 instances |
| **Total API Connections** | ~214 |
| **Unique modulCode** | 92 |

---

## Additional Notes

### Function Signature callApiFetch:
```dart
Future<Map<String, dynamic>?> callApiFetch({
  BuildContext? context,
  required String modulCode,
  String? modulParam,
  Map<String, dynamic>? additionalBody,
  bool debug = false,
})
```

### modulCode Categories:
- **Auth**: `bsCheckUser`, `apCheckUser`, `dashboardCheckUser`
- **User**: `getSnituser`, `saveUserBs`, `saveUserEnabled`, `resetImei`, `resetPassword`, `enableBs`
- **Vehicle**: `getTruck`, `saveTruckAvailable`, `saveTruckLokasi`, `saveNfcTruck`, `resetNfc`, `getLokasi`
- **Asset**: `getGenset`, `getSasis`, `getAsset` + variants
- **Inventory**: `invGetItemStockOpname`, `invGetSite`, `invGetItem`, `invSaveItemStockOpname`
- **POM**: `getPom`, `savePomEnabled`, `saveNfcPom`, `resetPumpNfc`, `NfcCheckMesin`, `savePomStock`
- **Driver**: `getDriver`, `saveDriverEnabled`, `saveDriverStatus`, `toGetDriverJob`, `toSaveDriverJob*`
- **BS**: `bsGetVerify`, `bsGetDone`, `bsGetApproval`, `bsSaveApproval`, `bsGetAmount`, `bsGetJO`, etc.
- **AP**: `apGetVendor`, `apGetData`, `apGetJO`
- **Dashboard**: `dashboardIN`, `dashboardStripping`, `dashboardStuffing`, `dashboardStrippingUpdate`
- **Sales**: `getSales`, `getCustomer`, `saveCustomerBlacklist`
- **Pantry**: `pantryGetSaldo`, `pantryGetOrder`, `pantrySaveOrder`, `pantryCancelOrder`
- **Accident**: `taGetAccident`, `taApprovalAccident`, `taDeleteAccident`, `toGetAccident`, `toApproveAccident`
- **Security**: `sgGetGateLog`, `sgGetTO`
- **Vessel**: `getVesselName`, `getVesselSchedule`, `getPortOrigin`, `getPortDestination`
- **Simulate**: `bsSimulasiGetJO`, `bsSimulasiGetAmount`
- **Hikvision**: `hikvisionGetDeviceRequest`, `createHikvisionUserRequest`, `deleteHikvisionUserRequest`, etc.
- **Lifecycle**: `saveUserHeartbeat`, `killHeartbeat`