@echo off
title Load Test - tridom.biz.id
color 0A

echo ============================================
echo   LOAD TEST - http://tridom.biz.id
echo ============================================
echo.

:: Cek apakah locust sudah terinstall
where locust >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] Locust belum terinstall. Menginstall sekarang...
    pip install locust
    echo.
)

echo Pilih mode:
echo   1. Web UI  (buka browser ke http://localhost:8089)
echo   2. Headless 200 users  - Warmup
echo   3. Headless 500 users  - Medium Stress
echo   4. Headless 1000 users - Heavy
echo   5. Headless 2000 users - Extreme
echo.
set /p PILIHAN="Masukkan pilihan (1-5): "

if "%PILIHAN%"=="1" (
    echo.
    echo [*] Menjalankan Web UI...
    echo [*] Buka browser ke http://localhost:8089
    echo [*] Tekan Ctrl+C untuk stop
    echo.
    locust -f load_test_windows.py --host http://tridom.biz.id
)

if "%PILIHAN%"=="2" (
    echo.
    echo [*] Menjalankan 200 users - Warmup...
    echo [*] Tekan Ctrl+C untuk stop
    echo.
    locust -f load_test_windows.py --headless -u 200 -r 20 --host http://tridom.biz.id --run-time 0
)

if "%PILIHAN%"=="3" (
    echo.
    echo [*] Menjalankan 500 users - Medium Stress...
    echo [*] Tekan Ctrl+C untuk stop
    echo.
    locust -f load_test_windows.py --headless -u 500 -r 50 --host http://tridom.biz.id --run-time 0
)

if "%PILIHAN%"=="4" (
    echo.
    echo [*] Menjalankan 1000 users - Heavy...
    echo [*] Tekan Ctrl+C untuk stop
    echo.
    locust -f load_test_windows.py --headless -u 1000 -r 100 --host http://tridom.biz.id --run-time 0
)

if "%PILIHAN%"=="5" (
    echo.
    echo [*] Menjalankan 2000 users - EXTREME...
    echo [*] Tekan Ctrl+C untuk stop
    echo.
    locust -f load_test_windows.py --headless -u 2000 -r 200 --host http://tridom.biz.id --run-time 0
)

pause
