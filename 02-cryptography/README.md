# 🔐 02 - Kriptografi Dasar



![Topik](https://img.shields.io/badge/Topik-Kriptografi-purple)
![Level](https://img.shields.io/badge/Level-Pemula-brightgreen)
![Status](https://img.shields.io/badge/Status-Done-success)



## 🤔 Apa itu Kriptografi?

Bayangkan kamu punya **surat rahasia** yang:
- Diacak hingga tidak terbaca orang lain
- Hanya penerima yang bisa membacanya
- Kalau diubah 1 huruf saja, langsung ketahuan

Itulah **Kriptografi!**  🔒

---

## 🔑 Apa itu Hashing?

Hashing adalah proses mengubah teks apapun
menjadi **kode unik dengan panjang tetap**.

| Input | Hash SHA-256 |
|-------|-------------|
| "Halo" | a3b2c1... |
| "halo" | f9e8d7... |

> ⚠️ Perhatikan: Beda 1 huruf besar/kecil = hash TOTALLY berbeda!

---

## 🌍 Contoh Penggunaan di Dunia Nyata

| Kegunaan | Penjelasan |
|----------|-----------|
| Password | Disimpan sebagai hash, bukan teks asli |
| Bitcoin | Setiap transaksi di-hash SHA-256 |
| Blockchain | Hash menghubungkan setiap block |

---

## 📄 File di Folder Ini

- `hashing.py` — Simulasi hashing SHA-256 dengan Python
  - Membuat fungsi hash sederhana
  - Membuktikan perubahan kecil = hash berbeda total

## ▶️ Cara Jalankan

### Persyaratan
- Python 3.x sudah terinstall

### Langkah-langkah
1. Download file `hashing.py`
2. Buka terminal/CMD
3. Ketik perintah:
```bash
python hashing.py
