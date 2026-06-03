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

## 🔐 Kenapa Blockchain Aman?

Karena setiap block **terhubung** ke block sebelumnya lewat hash.
Kalau ada yang coba ubah 1 data saja → semua hash berubah →
semua orang langsung tahu ada yang curang! 😎

---

## 📄 File di Folder Ini

- `simple_block.py` — Simulasi membuat blockchain sederhana dengan Python

## ▶️ Cara Jalankan
```bash
python simple_block.py
