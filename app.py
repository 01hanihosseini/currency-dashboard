import pandas as pd
import plotly.express as px
import streamlit as st


st.title("Currency Price Dashboard")
df = pd.read_csv("data/prices.csv", parse_dates=["time"])

fig = px.line(df, x="time" ,y= "price", color="coin", markers=True)
st.plotly_chart(fig, use_container_width=True)