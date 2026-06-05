import hashlib
import os

# ============================================
# DIGITAL SIGNATURE - Tanda Tangan Digital
# ============================================
# File ini mengajarkan:
# - Apa itu tanda tangan digital
# - Bagaimana membuktikan keaslian transaksi
# - Kenapa transaksi crypto tidak bisa dipalsukan
# ============================================

def buat_kunci_privat():
    # Kunci privat = password rahasia kamu
    return os.urandom(32).hex()

def buat_kunci_publik(kunci_privat):
    # Kunci publik = alamat wallet kamu
    return hashlib.sha256(kunci_privat.encode()).hexdigest()

def tanda_tangani(pesan, kunci_privat):
    # Tanda tangan = bukti bahwa KAMU yang kirim
    gabungan = pesan + kunci_privat
    return hashlib.sha256(gabungan.encode()).hexdigest()

def verifikasi(pesan, tanda_tangan, kunci_publik, kunci_privat):
    # Verifikasi = cek apakah tanda tangan valid
    tanda_tangan_asli = tanda_tangani(pesan, kunci_privat)
    return tanda_tangan == tanda_tangan_asli

# ============================================
# SIMULASI
# ============================================

print("🔐 Simulasi Tanda Tangan Digital\n")

# Budi buat kunci
kunci_privat_budi = buat_kunci_privat()
kunci_publik_budi = buat_kunci_publik(kunci_privat_budi)

print(f"🔑 Kunci Privat Budi : {kunci_privat_budi[:20]}... (RAHASIA!)")
print(f"🌐 Kunci Publik Budi : {kunci_publik_budi[:20]}... (Publik)")

# Budi kirim transaksi
pesan = "Budi kirim 1 BTC ke Ani"
tanda_tangan = tanda_tangani(pesan, kunci_privat_budi)

print(f"\n📝 Pesan      : {pesan}")
print(f"✍️  Tanda Tangan: {tanda_tangan[:20]}...")

# Verifikasi transaksi
hasil = verifikasi(pesan, tanda_tangan, kunci_publik_budi, kunci_privat_budi)
print(f"\n✅ Transaksi valid: {hasil}")

# Simulasi pemalsuan
print("\n⚠️  Simulasi: Hacker coba palsukan transaksi!")
pesan_palsu = "Hacker kirim 1 BTC ke dirinya sendiri"
hasil_palsu = verifikasi(pesan_palsu, tanda_tangan, kunci_publik_budi, kunci_privat_budi)
print(f"❌ Transaksi palsu valid: {hasil_palsu}")
print("\n🎉 Tanda tangan digital berhasil mencegah pemalsuan!")
