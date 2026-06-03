import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash="0"):
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hitung_hash()

    def hitung_hash(self):
        konten = self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(konten.encode()).hexdigest()

# Buat 3 block sederhana
block1 = Block("Transaksi: Budi kirim 1 BTC ke Ani")
block2 = Block("Transaksi: Ani kirim 0.5 BTC ke Cici", block1.hash)
block3 = Block("Transaksi: Cici kirim 0.1 BTC ke Dodi", block2.hash)

for b in [block1, block2, block3]:
    print(f"Data     : {b.data}")
    print(f"Hash     : {b.hash}")
    print(f"Prev Hash: {b.previous_hash}")
    print("-" * 60)
