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

## ⛓️ Apa itu Genesis Block?

Genesis Block adalah **block pertama** dalam sebuah blockchain.
- Tidak punya block sebelumnya
- Previous Hash-nya = "0"
- Ibarat **halaman pertama** dalam buku catatan blockchain


## ⛏️ Apa itu Proof of Work?

Bayangkan kamu diminta mencari **kombinasi angka** yang:
- Menghasilkan hash dengan awalan tertentu (misal: "000")
- Harus dicoba jutaan kali sampai ketemu
- Semakin banyak angka nol = semakin sulit

Itulah yang dilakukan komputer saat **mining Bitcoin!** 🖥️

| Difficulty | Target Hash | Estimasi Percobaan |
|------------|------------|-------------------|
| 1 | 0... | ~16 kali |
| 3 | 000... | ~4,096 kali |
| 4 | 0000... | ~65,536 kali |
| 6 | 000000... | ~16 juta kali |

---

## 💼 Apa itu Wallet?

| Komponen | Fungsi | Boleh Dibagikan? |
|----------|--------|-----------------|
| Private Key | Kunci rahasia wallet | ❌ JANGAN PERNAH! |
| Public Key | Turunan private key | ⚠️ Hati-hati |
| Alamat Wallet | Seperti nomor rekening | ✅ Aman |

---

## 🌳 Apa itu Merkle Tree?

Bayangkan kamu punya **pohon terbalik** dimana:
- Setiap daun = 1 transaksi
- Setiap cabang = gabungan hash 2 daun
- Akar pohon = **Merkle Root** (sidik jari semua transaksi)

Ubah 1 transaksi saja → seluruh pohon berubah! 🌿

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

- `proof_of_work.py` — Simulasi proses mining Bitcoin
  - Simulasi mining dengan tingkat kesulitan berbeda
  - Menghitung jumlah percobaan dan waktu mining
  - Membuktikan kenapa mining butuh energi besar

- `wallet_generator.py` — Membuat alamat wallet crypto
  - Generate private key & public key
  - Membuat alamat wallet unik
  - Penjelasan pentingnya menjaga private key

- `merkle_tree.py` — Struktur data dalam blockchain
  - Membuat Merkle Tree dari daftar transaksi
  - Membuktikan perubahan 1 transaksi = root berubah
  - Cara blockchain memverifikasi transaksi dengan cepat

## 🌍 Contoh Blockchain di Dunia Nyata

| Nama | Kegunaan |
|------|----------|
| Bitcoin | Mata uang digital |
| Ethereum | Smart contract & DeFi |
| Solana | Transaksi super cepat |
| Polygon | Biaya transaksi murah |

#### Persyaratan
- Python 3.x sudah terinstall di komputermu

### Langkah-langkah
1. Download file yang ingin dijalankan
2. Buka terminal/CMD di folder yang sama
3. Ketik perintah:

### 🔹 simple_block.py
```bash
python simple_block.py
```
### 🔹 simple_chain.py
```bash
python simple_chain.py
```
### 🔹 proof_of_work.py
```bash
python proof_of_work.py
```
### 🔹 wallet_generator.py
```bash
python wallet_generator.py
```
### 🔹 merkle_tree.py
```bash
python merkle_tree.py
```



