import pandas as pd
import plotly.express as px
import streamlit as st
from fetcher import get_prices, save_price
from alerts import check_change


COINS = ["bitcoin", "ethereum", "solana"]

st.title("Currency Price Dashboard")

st.sidebar.header("Settings")
selected = st.sidebar.multiselect("Coins", COINS, default=["bitcoin"])
threshold = st.sidebar.slider("Alert threshold (%)", 0.01, 5.0, 0.1)
window = st.sidebar.slider("Alert window (minutes)", 1, 30, 5)
refresh = st.sidebar.slider("Refresh every (second)", 15, 120, 30)


@st.cache_data(ttl=60)
def cached_prices(coins):
    return get_prices(list(coins))


@st.fragment(run_every=refresh)
def live_chart():
    if not selected:
        st.info("Select at least one coin from the sidebar.")
        return

    for coin in selected:
        try:
            prices = cached_prices(tuple(selected))
            for coin , price in prices.items():
                save_price(coin, price)
                st.metric(f"{coin.title()} (USD)", f"{price:,}")
        except Exception as e:
            st.warning(f"Could not fetch {coin}: {e}")

    df = pd.read_csv("data/prices.csv", parse_dates=["time"])
    df = df[df["coin"].isin(selected)]
    df = df[df["time"] >= df["time"].max() - pd.Timedelta(hours=1)]

    for coin in selected:
        change = check_change(df, coin, threshold, minutes=window)
        if change is not None:
            st.error(f"{coin.title()} changed {change:+.2f}% in the last {window} minutes")

    fig = px.line(df, x="time" ,y= "price", color="coin", markers=True, facet_row="coin", height=300 * len(selected))
    fig.update_yaxes(matches= None)
    st.plotly_chart(fig, use_container_width=True)

live_chart()