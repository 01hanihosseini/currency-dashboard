import requests
import os
from datetime import datetime
import pandas as pd


def get_price(coin="bitcoin", currency = "usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": currency}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data[coin][currency]



def save_price(coin, price, path="data/prices.csv"):
    row = pd.DataFrame([{
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "coin": coin, 
        "price": price,
    }])
    row.to_csv(path, mode="a", header=not os.path.exists(path), index=False)



if __name__ == "__main__":
    price = get_price()
    print(price)
    save_price("bitcoin", price)