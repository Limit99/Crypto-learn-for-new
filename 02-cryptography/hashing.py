import hashlib

def hash_sha256(teks):
    return hashlib.sha256(teks.encode()).hexdigest()

# Contoh hashing
pesan = "Halo, ini transaksi Bitcoin!"
print(f"Pesan asli : {pesan}")
print(f"Hash SHA256: {hash_sha256(pesan)}")

# Coba ubah 1 huruf saja
pesan2 = "halo, ini transaksi Bitcoin!"
print(f"\nPesan asli : {pesan2}")
print(f"Hash SHA256: {hash_sha256(pesan2)}")

print("\n⚠️ Perhatikan: 1 huruf beda = hash TOTALLY berbeda!")
