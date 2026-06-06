import hashlib

# ============================================
# MERKLE TREE - Struktur Data Blockchain
# ============================================
# File ini mengajarkan:
# - Apa itu Merkle Tree
# - Bagaimana transaksi diorganisir dalam block
# - Kenapa Merkle Tree membuat blockchain efisien
# - Cara memverifikasi transaksi dengan cepat
# ============================================

def hash_data(data):
    """Fungsi hashing sederhana"""
    return hashlib.sha256(data.encode()).hexdigest()

def buat_merkle_tree(transaksi):
    """Membuat Merkle Tree dari daftar transaksi"""
    
    if len(transaksi) == 0:
        return None
    
    # Level 0: Hash semua transaksi
    level = [hash_data(tx) for tx in transaksi]
    
    print("\n🌿 Level 0 (Transaksi):")
    for i, tx in enumerate(transaksi):
        print(f"   TX{i+1}: {tx}")
        print(f"   Hash: {level[i][:20]}...")
    
    tingkat = 1
    while len(level) > 1:
        level_baru = []
        
        # Kalau jumlah ganjil, duplikat yang terakhir
        if len(level) % 2 == 1:
            level.append(level[-1])
        
        # Gabungkan setiap pasangan hash
        for i in range(0, len(level), 2):
            gabungan = level[i] + level[i+1]
            hash_baru = hash_data(gabungan)
            level_baru.append(hash_baru)
        
        print(f"\n🌿 Level {tingkat}:")
        for h in level_baru:
            print(f"   Hash: {h[:20]}...")
        
        level = level_baru
        tingkat += 1
    
    return level[0]

# ============================================
# SIMULASI
# ============================================

print("=" * 50)
print("  🌳 MERKLE TREE SIMULATOR")
print("=" * 50)

# Daftar transaksi dalam 1 block
transaksi = [
    "Budi kirim 1 BTC ke Ani",
    "Ani kirim 0.5 ETH ke Cici",
    "Cici kirim 100 USDT ke Dodi",
    "Dodi kirim 0.1 SOL ke Eko"
]

print(f"\n📦 Block berisi {len(transaksi)} transaksi:")

# Buat Merkle Tree
merkle_root = buat_merkle_tree(transaksi)

print(f"\n🌳 Merkle Root (Akar):")
print(f"   {merkle_root}")

print("\n💡 Kesimpulan:")
print("✅ Merkle Root = sidik jari SEMUA transaksi dalam block")
print("✅ Ubah 1 transaksi = Merkle Root berubah total")
print("✅ Memudahkan verifikasi tanpa cek semua transaksi")
