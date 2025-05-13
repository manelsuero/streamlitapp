import streamlit as st
import requests

st.title("📉 Crypto Alert System")

crypto = st.text_input("Enter a cryptocurrency (e.g., BTC)")  
fiat = st.text_input("Enter a fiat currency (e.g., EUR)")     
threshold = st.number_input("Enter a price threshold", min_value=0.0, step=0.01)

if st.button("Notify me"):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={crypto}&convert={fiat}"
    headers = {
        "X-CMC_PRO_API_KEY": st.secrets["API_KEY"],
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    try:
        price = data["data"][crypto.upper()]["quote"][fiat.upper()]["price"]
        st.write(f"The current price of {crypto.upper()} is {price:,.2f} {fiat.upper()}.")
        st.write(f"We will notify you when the price reaches {threshold:,.2f} {fiat.upper()}.")
    except:
        st.error("There was an error. Maybe you wrote the wrong crypto or fiat symbol.")
