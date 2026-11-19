import requests
import os
from datetime import datetime
import pandas as pd



def save_price(coin, price, path="data/prices.csv"):
    row = pd.DataFrame([{
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "coin": coin, 
        "price": price,
    }])
    row.to_csv(path, mode="a", header=not os.path.exists(path), index=False)


def get_prices(coins, currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(coins), "vs_currencies": currency}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return {coin: data[coin][currency] for coin in coins}


if __name__ == "__main__":
    prices = get_prices(["bitcoin", "ethereum"])
    print(prices)
    for coin, price in prices.items():
        save_price(coin, price)
