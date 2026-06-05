import hashlib
import datetime

# ============================================
# SIMPLE CHAIN - Belajar cara kerja blockchain
# ============================================
# File ini mengajarkan:
# - Bagaimana blok saling terhubung
# - Kenapa blockchain tidak bisa dimanipulasi
# - Apa yang terjadi kalau ada yang curang
# ============================================

class Block:
    def __init__(self, data, previous_hash="0"):
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hitung_hash()

    def hitung_hash(self):
        konten = self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(konten.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.buat_genesis_block()

    def buat_genesis_block(self):
        # Genesis block = block pertama dalam blockchain
        genesis = Block("Genesis Block - Awal dari segalanya")
        self.chain.append(genesis)
        print("✅ Genesis Block berhasil dibuat!")

    def tambah_block(self, data):
        block_sebelumnya = self.chain[-1]
        block_baru = Block(data, block_sebelumnya.hash)
        self.chain.append(block_baru)
        print(f"✅ Block baru ditambahkan: {data}")

    def cek_validitas(self):
        print("\n🔍 Mengecek validitas blockchain...")
        for i in range(1, len(self.chain)):
            block_sekarang = self.chain[i]
            block_sebelumnya = self.chain[i-1]

            # Cek apakah hash block masih valid
            if block_sekarang.hash != block_sekarang.hitung_hash():
                print(f"❌ Block {i} telah dimanipulasi!")
                return False

            # Cek apakah sambungan antar block masih valid
            if block_sekarang.previous_hash != block_sebelumnya.hash:
                print(f"❌ Sambungan block {i} terputus!")
                return False

        print("✅ Blockchain valid! Semua block terhubung dengan benar.")
        return True

    def tampilkan_chain(self):
        print("\n📦 Isi Blockchain:")
        print("=" * 60)
        for i, block in enumerate(self.chain):
            print(f"Block #{i}")
            print(f"Data         : {block.data}")
            print(f"Hash         : {block.hash[:20]}...")
            print(f"Previous Hash: {block.previous_hash[:20]}...")
            print("-" * 60)

# ============================================
# SIMULASI
# ============================================

# Buat blockchain baru
print("🚀 Membuat Blockchain Baru...")
blockchain = Blockchain()

# Tambah beberapa transaksi
blockchain.tambah_block("Budi kirim 1 BTC ke Ani")
blockchain.tambah_block("Ani kirim 0.5 ETH ke Cici")
blockchain.tambah_block("Cici kirim 100 USDT ke Dodi")

# Tampilkan semua block
blockchain.tampilkan_chain()

# Cek validitas
blockchain.cek_validitas()

# Simulasi manipulasi data
print("\n⚠️  Simulasi: Ada yang coba manipulasi data!")
blockchain.chain[1].data = "Budi kirim 100 BTC ke Hacker!"
print("Data block #1 berhasil diubah oleh hacker!")

# Cek validitas setelah dimanipulasi
blockchain.cek_validitas()
