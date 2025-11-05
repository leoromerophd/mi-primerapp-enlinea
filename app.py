import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sb


st.title("Mi primer app en línea")
# 
ticker =  st.text_input("Ingresa el  Símbolo del Ticker", value="AAPL")

if ticker:
    data =  yf.download(ticker, period="1y")
    st.write(f"Datos de {ticker}:")
    st.dataframe(data.tail())

    fig, ax = plt.subplots()
    ax.plot(data.index, data["Close"], label="Cierre", color="blue")
    ax.set_title(f"Precio de cierre de {ticker} - Último año")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Precio (USD)")
    ax.legend()
    st.pyplot(fig)