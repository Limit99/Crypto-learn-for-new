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

## ▶️ Cara Jalankan

### Persyaratan
- Python 3.x sudah terinstall
- Koneksi internet aktif

### Langkah-langkah
1. Download file `fetch_prices.py`
2. Buka terminal/CMD
3. Ketik perintah:
```bash
python fetch_prices.py
