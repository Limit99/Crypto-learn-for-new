import urllib.request
import json

# ============================================
# PRICE ALERT - Notifikasi Harga Crypto
# ============================================
# File ini mengajarkan:
# - Cara memantau harga crypto secara otomatis
# - Memberi notifikasi kalau harga naik/turun
# - Simulasi sistem alert seperti di Pintu/Tokocrypto
# ============================================

def ambil_harga(koin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={koin}&vs_currencies=usd"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data[koin]["usd"]

def cek_alert(koin, harga_sekarang, batas_atas, batas_bawah):
    print(f"\n💰 Harga {koin.upper()} sekarang: ${harga_sekarang:,}")
    
    if harga_sekarang >= batas_atas:
        print(f"🚀 ALERT! Harga naik melewati ${batas_atas:,}!")
        print(f"   Ini saat yang baik untuk JUAL!")
    elif harga_sekarang <= batas_bawah:
        print(f"📉 ALERT! Harga turun di bawah ${batas_bawah:,}!")
        print(f"   Ini saat yang baik untuk BELI!")
    else:
        print(f"😴 Harga masih normal.")
        print(f"   Batas atas : ${batas_atas:,}")
        print(f"   Batas bawah: ${batas_bawah:,}")

# ============================================
# KONFIGURASI 4 KOIN
# ============================================

koin_config = [
    {
        "nama": "bitcoin",
        "batas_atas": 120000,
        "batas_bawah": 90000
    },
    {
        "nama": "ethereum",
        "batas_atas": 5000,
        "batas_bawah": 2000
    },
    {
        "nama": "solana",
        "batas_atas": 300,
        "batas_bawah": 100
    },
    {
        "nama": "matic-network",
        "batas_atas": 2,
        "batas_bawah": 0.5
    }
]

# ============================================
# SIMULASI
# ============================================

print("🔔 Sistem Price Alert Crypto")
print("Memantau 4 koin sekaligus...\n")
print("=" * 40)

for koin in koin_config:
    print(f"\n📊 Mengecek {koin['nama'].upper()}...")
    harga = ambil_harga(koin["nama"])
    cek_alert(koin["nama"], harga, koin["batas_atas"], koin["batas_bawah"])
    print("-" * 40)
