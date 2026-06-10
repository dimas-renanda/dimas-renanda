# TRADING.md — Dante Trading System

## ⚠️ BACA INI SETIAP ADA PESAN TRADING DI WA

Dim punya sistem trading futures semi-otomatis via Binance API.

## Cara Kerja

1. Cron job Dante scan market tiap 30 menit
2. Kirim signal ke WA Dim (+6285155102105)
3. **Dim reply YES atau NO**
4. Kalau YES → **kamu eksekusi trade langsung via script**
5. Kalau NO → hapus pending signal, skip

## Ketika Dim Reply "YES" di WA

1. Baca file pending signal: `~/.dante-trading/pending_signal.json`
2. Jalankan via exec:
   ```
   python3.13 /Users/user/.dante-trading/trade.py trade [SYMBOL] [DIRECTION] [SIZING] [LEVERAGE] [TP_PCT] [SL_PCT]
   ```
3. Kirim konfirmasi ke WA Dim bahwa order sudah masuk
4. Hapus file pending_signal.json

## Ketika Dim Reply "NO" di WA

1. Hapus file `~/.dante-trading/pending_signal.json`
2. Reply singkat: "Signal di-skip ✅"

## Script Trading

- **Lokasi:** `/Users/user/.dante-trading/trade.py`
- **Python:** `python3.13`
- **API:** Binance Futures (sudah tersimpan di script)
- **Perintah:**
  ```bash
  # Eksekusi live trade
  python3.13 /Users/user/.dante-trading/trade.py trade SOLUSDT SHORT 0.15 5 0.022 0.019

  # Cek status & posisi
  python3.13 /Users/user/.dante-trading/trade.py status

  # Paper trade (simulasi)
  python3.13 /Users/user/.dante-trading/trade.py paper SOLUSDT SHORT 0.15 5 0.022 0.019

  # Close semua posisi darurat
  python3.13 /Users/user/.dante-trading/trade.py close
  ```

## Format Argumen

```
trade [SYMBOL] [DIRECTION] [SIZING_PCT] [LEVERAGE] [TP_PCT] [SL_PCT]

Contoh:
SYMBOL     = SOLUSDT, HYPEUSDT, ADAUSDT, dll
DIRECTION  = SHORT atau LONG
SIZING_PCT = 0.15 (= 15% dari balance)
LEVERAGE   = 5 atau 7
TP_PCT     = 0.031 (= 3.1%)
SL_PCT     = 0.021 (= 2.1%)
```

## File Pending Signal

Setiap kali cron kirim signal ke WA, file ini ditulis:
`~/.dante-trading/pending_signal.json`

```json
{
  "symbol": "HYPEUSDT",
  "direction": "SHORT",
  "sizing_pct": 0.15,
  "leverage": 5,
  "tp_pct": 0.031,
  "sl_pct": 0.021,
  "confidence": 67,
  "entry_zone": "38.80-39.20",
  "sent_at": "16:11 WIB"
}
```

## Aturan Wajib

- Max loss/hari: 3% total modal → STOP semua trading
- Jangan buka 2 posisi bersamaan
- Leverage max 10x
- Confidence <65% = tidak ada signal yang dikirim
- No trade setelah 22:00 WIB
- Jangan hold posisi semalaman
