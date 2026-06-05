# 🧱 01 - Blockchain Learning
![Topic](https://img.shields.io/badge/Topik-Blockchain-orange?logo=bitcoin)
![Level](https://img.shields.io/badge/Level-Pemula-brightgreen)


## 🤔 Apa itu Blockchain?

Bayangkan kamu punya **buku catatan** yang:
- Setiap halaman berisi catatan transaksi
- Setiap halaman terhubung ke halaman sebelumnya
- Tidak bisa dihapus atau diubah oleh siapapun
- Dipegang oleh ribuan orang sekaligus

Itulah **Blockchain!** 🔗⛓️

---

## 🧩 Bagian-bagian Sebuah Block

Setiap block berisi 4 hal:
| Bagian | Penjelasan |
|--------|-----------|
| Data | Isi transaksi (siapa kirim ke siapa) |
| Hash | Sidik jari unik block ini |
| Previous Hash | Sidik jari block sebelumnya |
| Timestamp | Waktu transaksi terjadi |

---

## 📄 File di Folder Ini

- `simple_block.py` — Simulasi membuat blockchain sederhana dengan Python
  - Membuat class Block dengan data, hash, dan timestamp
  - Merangkai 3 block menjadi blockchain mini
  - Membuktikan setiap block terhubung lewat hash
 
- `simple_chain.py` — Simulasi blockchain lengkap dengan validasi
  - Membuat Genesis Block (block pertama)
  - Merangkai banyak block menjadi blockchain
  - Mengecek validitas seluruh chain
  - Simulasi apa yang terjadi kalau ada yang manipulasi data

## ▶️ Cara Jalankan
### 🔹 simple_block.py
```bash
python simple_block.py
```
### 🔹 simple_chain.py
```bash

python simple_chain.py
```

## 🌍 Contoh Blockchain di Dunia Nyata

| Nama | Kegunaan |
|------|----------|
| Bitcoin | Mata uang digital |
| Ethereum | Smart contract & DeFi |
| Solana | Transaksi super cepat |
| Polygon | Biaya transaksi murah |

## ⛓️ Apa itu Genesis Block?

Genesis Block adalah **block pertama** dalam sebuah blockchain.
- Tidak punya block sebelumnya
- Previous Hash-nya = "0"
- Ibarat **halaman pertama** dalam buku catatan blockchain
