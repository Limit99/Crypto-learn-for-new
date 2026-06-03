import urllib.request
import json

def cek_harga(koin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={koin}&vs_currencies=usd,idr"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    harga_usd = data[koin]["usd"]
    harga_idr = data[koin]["idr"]
    
    print(f"\n💰 Harga {koin.upper()}")
    print(f"   USD : ${harga_usd:,}")
    print(f"   IDR : Rp{harga_idr:,}")

# Cek harga beberapa koin
for koin in ["bitcoin", "ethereum", "solana"]:
    cek_harga(koin)
