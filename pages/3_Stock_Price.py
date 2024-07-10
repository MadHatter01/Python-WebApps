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

col1, col2 = st.columns(2)
with col1:
    st.subheader("Volume Chart")
    fig, ax = plt.subplots()
    ax.bar(df.index, df['Volume'])
    ax.set_xlabel('Date')
    plt.xticks(rotation=45)
    ax.set_ylabel('Volume')
    ax.set_title(f'Trading volume of {stock_symbol.upper()} over the last one month')
    st.pyplot(fig)
    st.bar_chart(df['Volume'])
    
    



with col2:
    
    st.subheader("Closing Price Chart")
    fig, ax = plt.subplots()

    ax.plot(df.index, df['Close'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.set_title(f'Closing price of {stock_symbol.upper()} over the last one month')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    st.line_chart(df['Close'])
    