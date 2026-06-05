# ============================================
# YIELD CALCULATOR - Hitung Keuntungan DeFi
# ============================================
# File ini mengajarkan:
# - Apa itu APY dan APR di DeFi
# - Cara menghitung keuntungan staking/farming
# - Perbandingan keuntungan vs deposito bank
# ============================================

def hitung_apr(modal, apr_persen, hari):
    """Hitung keuntungan APR (tanpa compound)"""
    keuntungan = modal * (apr_persen/100) * (hari/365)
    return keuntungan

def hitung_apy(modal, apy_persen, hari):
    """Hitung keuntungan APY (dengan compound/bunga berbunga)"""
    hasil = modal * ((1 + apy_persen/100) ** (hari/365))
    keuntungan = hasil - modal
    return keuntungan

def tampilkan_hasil(nama, modal, keuntungan, hari):
    total = modal + keuntungan
    print(f"\n📊 {nama}")
    print(f"   Modal awal  : Rp{modal:,.0f}")
    print(f"   Keuntungan  : Rp{keuntungan:,.0f}")
    print(f"   Total {hari} hari: Rp{total:,.0f}")

# ============================================
# SIMULASI
# ============================================

print("💰 Kalkulator Keuntungan DeFi\n")
print("=" * 40)

modal = 10_000_000  # Rp 10 juta
hari = 365          # 1 tahun

print(f"Modal    : Rp{modal:,.0f}")
print(f"Periode  : {hari} hari (1 tahun)")
print("=" * 40)

# Deposito Bank (rata-rata 3-4% per tahun)
keuntungan_bank = hitung_apr(modal, 3.5, hari)
tampilkan_hasil("🏦 Deposito Bank (APR 3.5%)",
    modal, keuntungan_bank, hari)

# Staking ETH (rata-rata 4-6% APY)
keuntungan_eth = hitung_apy(modal, 5, hari)
tampilkan_hasil("💎 Staking Ethereum (APY 5%)",
    modal, keuntungan_eth, hari)

# Liquidity Pool (rata-rata 10-20% APY)
keuntungan_lp = hitung_apy(modal, 15, hari)
tampilkan_hasil("🔄 Liquidity Pool (APY 15%)",
    modal, keuntungan_lp, hari)

# Yield Farming (rata-rata 20-50% APY)
keuntungan_farm = hitung_apy(modal, 30, hari)
tampilkan_hasil("🌾 Yield Farming (APY 30%)",
    modal, keuntungan_farm, hari)

print("\n" + "=" * 40)
print("⚠️  DISCLAIMER:")
print("Angka di atas hanya simulasi.")
print("DeFi mengandung risiko tinggi.")
print("Selalu DYOR (Do Your Own Research)!")
