import pandas as pd
import plotly.express as px
import streamlit as st
from fetcher import get_price, save_price
from alerts import check_change



st.title("Currency Price Dashboard")

threshold = st.sidebar.slider("Alert threshold (%)", 0.01, 5.0, 0.1)

@st.fragment(run_every=30)
def live_chart():
    try:
        price = get_price()
        save_price("bitcoin", price)
        st.metric("Bitcoin (USD)", f"{price:,}")
    except Exception as e:
        st.warning(f"Could not fetch price: {e}")

    df = pd.read_csv("data/prices.csv", parse_dates=["time"])

    change = check_change(df, "bitcoin", threshold, minutes=5)
    if change is not None:
        st.error(f"Bitcoin changed {change:+.2f}% in the last 5 minutes")

    fig = px.line(df, x="time" ,y= "price", color="coin", markers=True)
    st.plotly_chart(fig, use_container_width=True)

live_chart()