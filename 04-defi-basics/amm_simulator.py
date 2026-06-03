# Simulasi AMM (Automated Market Maker) seperti Uniswap

class LiquidityPool:
    def __init__(self, token_a, token_b):
        self.token_a = token_a  # contoh: ETH
        self.token_b = token_b  # contoh: USDT
        print(f"Pool dibuat: {token_a} ETH & {token_b} USDT")
        print(f"Harga awal: 1 ETH = {token_b/token_a} USDT\n")

    def beli_eth(self, usdt_masuk):
        eth_keluar = (self.token_a * usdt_masuk) / (self.token_b + usdt_masuk)
        self.token_b += usdt_masuk
        self.token_a -= eth_keluar
        harga_baru = self.token_b / self.token_a
        print(f"Kamu masukkan : {usdt_masuk} USDT")
        print(f"Kamu dapat    : {eth_keluar:.4f} ETH")
        print(f"Harga ETH baru: {harga_baru:.2f} USDT\n")

# Simulasi
pool = LiquidityPool(token_a=10, token_b=20000)
pool.beli_eth(1000)
pool.beli_eth(5000)
