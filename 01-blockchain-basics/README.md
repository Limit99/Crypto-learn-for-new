# 🧱 01 - Blockchain Learning
![Topic](https://img.shields.io/badge/Topik-Blockchain-orange?logo=bitcoin)


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

## ▶️ Cara Jalankan

### Persyaratan
- Python 3.x sudah terinstall di komputermu

### Langkah-langkah
1. Download file `simple_block.py`
2. Buka terminal/CMD di folder yang sama
3. Ketik perintah berikut:
```bash
python simple_block.py
