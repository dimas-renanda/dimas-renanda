# MEMORY.md — Dante's Long-Term Memory

## Dim (User)
- Nama: Dimas Renanda
- WA: +6285155102105
- Timezone: Asia/Jakarta (GMT+7)
- GitHub CLI: username `dimas-renanda`
- Bekerja di PT Tri Dominitama, Jl. Kalianak Barat 55E, Surabaya (logistik cold chain)

## VSCode
- GitHub Copilot Chat error `Cannot read properties of undefined (reading 'bind')` → fix: hapus `~/.vscode/extensions/github.copilot-chat-*` yang versi manual, biar versi built-in bawaan VSCode yang jalan. Jangan install Copilot Chat secara manual kalau VSCode sudah bundle built-in.

## Sistem & Tools
- Trading bot DANTE: cron job di OpenClaw, script di `/Users/user/.dante-trading/`
  - Bot dimatikan pada 19 Mei 2026 (balance drop, Dim minta stop)
  - Script utama: `auto_trade.py` (scan CoinGecko + eksekusi Binance Futures)
  - Python: `/usr/local/bin/python3.13`
  - OpenClaw CLI: `/Users/user/.nvm/versions/node/v22.17.0/bin/openclaw`
- Morning Brief cron: tiap 09:00 WIB, kirim ke WA Dim (job id: 7bb18227)
