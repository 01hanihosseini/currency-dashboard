import pandas as pd

def  check_change(df, coin, treshold_pct, minutes =5):
    data = df[df["coin"] == coin]
    if len(data) < 2:
        return None
    latest = data.iloc[-1]
    cutoff = latest["time"] - pd.Timedelta(minutes=minutes)
    old = data[data["time"] <= cutoff]
    if old.empty:
        return None
    old_price = old.iloc[-1]["price"]
    change = (latest["price"] - old_price) / old_price * 100
    return change if abs (change) >= treshold_pct else None