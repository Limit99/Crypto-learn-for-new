import hashlib
import time

# ============================================
# PROOF OF WORK - Simulasi Mining Bitcoin
# ============================================
# File ini mengajarkan:
# - Apa itu Proof of Work (POW)
# - Bagaimana proses mining bekerja
# - Kenapa mining membutuhkan banyak energi
# - Apa itu difficulty (tingkat kesulitan)
# ============================================

def mining(data, difficulty):
    print(f"\n⛏️  Mulai mining...")
    print(f"🎯 Target: hash harus dimulai dengan {'0' * difficulty}")
    print(f"📦 Data  : {data}\n")
    
    nonce = 0
    target = "0" * difficulty
    waktu_mulai = time.time()
    
    while True:
        teks = data + str(nonce)
        hash_result = hashlib.sha256(teks.encode()).hexdigest()
        
        if hash_result.startswith(target):
            waktu_selesai = time.time()
            durasi = waktu_selesai - waktu_mulai
            print(f"✅ Block berhasil di-mining!")
            print(f"🔢 Nonce ditemukan : {nonce}")
            print(f"#️⃣  Hash           : {hash_result}")
            print(f"⏱️  Waktu mining   : {durasi:.2f} detik")
            print(f"🔄 Total percobaan : {nonce + 1:,} kali")
            return hash_result
        
        nonce += 1
        
        # Tampilkan progress setiap 100,000 percobaan
        if nonce % 100_000 == 0:
            print(f"⏳ Sudah mencoba {nonce:,} kombinasi...")

# ============================================
# SIMULASI
# ============================================

print("=" * 50)
print("  ⛏️  SIMULASI MINING BITCOIN")
print("=" * 50)

# Mining dengan difficulty rendah (mudah)
print("\n🟢 Difficulty 1 (Mudah):")
mining("Block #1 - Budi kirim 1 BTC ke Ani", difficulty=1)

# Mining dengan difficulty sedang
print("\n🟡 Difficulty 3 (Sedang):")
mining("Block #2 - Ani kirim 0.5 ETH ke Cici", difficulty=3)

# Mining dengan difficulty tinggi
print("\n🔴 Difficulty 4 (Sulit):")
mining("Block #3 - Cici kirim 100 USDT ke Dodi", difficulty=4)

print("\n💡 Kesimpulan:")
print("Semakin tinggi difficulty = semakin lama mining")
print("Inilah kenapa mining Bitcoin butuh komputer canggih!")
