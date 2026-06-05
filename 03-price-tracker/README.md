# 📈 03 - Price Tracker



![Topik](https://img.shields.io/badge/Topik-Price_Tracker-blue)
![Level](https://img.shields.io/badge/Level-Pemula-brightgreen)
![Status](https://img.shields.io/badge/Status-Done-success)



## 🤔 Apa itu Price Tracker?

Bayangkan kamu punya **asisten pribadi** yang:
- Memantau harga Bitcoin setiap saat
- Memberitahu harga dalam USD dan Rupiah
- Bisa dicek kapan saja secara otomatis

Itulah **Price Tracker!** 📊

---

## 🌐 Apa itu API?

API adalah jembatan antara aplikasi kita
dengan sumber data di internet.

| Tanpa API | Dengan API |
|-----------|-----------|
| Cek harga manual | Otomatis real-time |
| Buka website dulu | Langsung dari kode |
| Tidak bisa diproses | Bisa diolah bebas |

---

## 🌍 Contoh Penggunaan di Dunia Nyata

| Aplikasi | Kegunaan |
|----------|---------|
| Pintu | Cek harga crypto IDR |
| Tokocrypto | Pantau pergerakan harga |
| CoinGecko | Data harga semua koin |

---

## 📄 File di Folder Ini

- `fetch_prices.py` — Mengambil harga crypto secara live
  - Koneksi ke API CoinGecko
  - Menampilkan harga dalam USD dan IDR
  - Bisa dicek untuk Bitcoin, Ethereum, Solana
- `price_alert.py` — Sistem notifikasi harga crypto otomatis
  - Memantau 4 koin sekaligus (BTC, ETH, SOL, MATIC)
  - Alert otomatis kalau harga naik atau turun
  - Simulasi sistem alert seperti di Pintu & Tokocrypto

## 🔔 Apa itu Price Alert?

Bayangkan kamu punya **asisten pribadi** yang:
- Memantau harga crypto 24 jam
- Memberitahu kalau harga naik drastis → saatnya JUAL
- Memberitahu kalau harga turun drastis → saatnya BELI

Itulah **Price Alert!** 📲

| Koin | Batas Atas | Batas Bawah |
|------|-----------|-------------|
| Bitcoin | $120,000 | $90,000 |
| Ethereum | $5,000 | $2,000 |
| Solana | $300 | $100 |
| Polygon | $2 | $0.5 |

## ▶️ Cara Jalankan

### Persyaratan
- Python 3.x sudah terinstall
- Koneksi internet aktif

### Langkah-langkah
1. Download file `fetch_prices.py`
2. Buka terminal/CMD
3. Ketik perintah:
### 🔹 fetch_prices.py
```bash
python fetch_prices.py
```
### 🔹 price_alert.py
```bash
python price_alert.py
