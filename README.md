# Currency Price Dashboard

A live cryptocurrency price dashboard with change alerts, built with Python, pandas and Streamlit.

## Features
- Live price charts that refresh automatically
- Multi-coin support (Bitcoin, Ethereum, Solana)
- Alerts when price changes beyond a set percentage
- Adjustable threshold, alert window and refresh rate
- Price history saved to CSV

## Tech Stack
Python, pandas, Streamlit, Plotly, CoinGecko API

## Setup
bash
git clone https://github.com/01hanihosseini/currency-dashboard.git
cd currency-dashboard
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
## Project Structure
- app.py — Streamlit interface
- fetcher.py — fetches and saves prices
- alerts.py — price change alert logic

## License
MIT