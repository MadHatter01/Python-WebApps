import streamlit as st
import yfinance as yf

import matplotlib.pyplot as plt

st.title("Data Visualization")

st.sidebar.header("User Input")
stock_symbol = st.sidebar.text_input("Enter a stock symbol", value = "COST")
data = yf.Ticker(stock_symbol)

df = data.history(period="1mo")

st.subheader(f"Stock data for {stock_symbol.upper()}")
st.write(df)

st.subheader("Volume Chart")
fig, ax = plt.subplots()
ax.bar(df.index, df['Volume'])
ax.set_xlabel('Date')
plt.xticks(rotation=45)
ax.set_ylabel('Volume')
ax.set_title(f'Trading volume of {stock_symbol.upper()} over the last one month')
st.pyplot(fig)