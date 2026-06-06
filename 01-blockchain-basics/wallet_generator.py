import hashlib
import os

# ============================================
# WALLET GENERATOR - Buat Alamat Wallet Crypto
# ============================================
# File ini mengajarkan:
# - Apa itu private key & public key
# - Bagaimana alamat wallet dibuat
# - Kenapa setiap wallet unik
# - Pentingnya menjaga private key
# ============================================

def buat_private_key():
    """Private key = kunci rahasia wallet kamu"""
    return os.urandom(32).hex()

def buat_public_key(private_key):
    """Public key = turunan dari private key"""
    return hashlib.sha256(private_key.encode()).hexdigest()

def buat_alamat_wallet(public_key):
    """Alamat wallet = versi pendek dari public key"""
    hash1 = hashlib.sha256(public_key.encode()).hexdigest()
    hash2 = hashlib.new('sha256', bytes.fromhex(hash1)).hexdigest()
    return "0x" + hash2[:40]

def tampilkan_wallet(nama):
    print(f"\n👤 Wallet milik: {nama}")
    print("-" * 60)
    
    private_key = buat_private_key()
    public_key = buat_public_key(private_key)
    alamat = buat_alamat_wallet(public_key)
    
    print(f"🔴 Private Key : {private_key}")
    print(f"   ⚠️  JANGAN PERNAH BAGIKAN KE SIAPAPUN!")
    print(f"🟢 Public Key  : {public_key[:40]}...")
    print(f"🔵 Alamat      : {alamat}")
    print(f"   ✅ Aman untuk dibagikan ke orang lain")

# ============================================
# SIMULASI
# ============================================

print("=" * 60)
print("  💼 WALLET GENERATOR")
print("=" * 60)

# Buat wallet untuk 3 orang
tampilkan_wallet("Budi")
tampilkan_wallet("Ani")
tampilkan_wallet("Cici")

print("\n" + "=" * 60)
print("💡 Kesimpulan:")
print("✅ Setiap wallet memiliki alamat yang UNIK")
print("✅ Private key → Public key → Alamat wallet")
print("❌ Tidak bisa balik dari Alamat → Private key")
print("🔐 Jaga private key seperti password rekening bank!")
