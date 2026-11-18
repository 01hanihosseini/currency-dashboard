import pandas as pd
import plotly.express as px
import streamlit as st
from fetcher import get_price, save_price


st.title("Currency Price Dashboard")

@st.fragment(run_every=30)
def live_chart():
    try:
        price = get_price()
        save_price("bitcoin", price)
        st.metric("Bitcoin (USD)", f"{price:,}")
    except Exception as e:
        st.warning(f"Could not fetch price: {e}")

    df = pd.read_csv("data/prices.csv", parse_dates=["time"])

    fig = px.line(df, x="time" ,y= "price", color="coin", markers=True)
    st.plotly_chart(fig, use_container_width=True)

live_chart()