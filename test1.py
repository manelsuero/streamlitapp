import streamlit as st

st.title("📈 Stock Analyzer with AI")

# Sidebar
st.sidebar.header("Options")
ticker = st.sidebar.text_input("Enter a stock ticker", value="AAPL")

# Secciones
st.header("🔍 Technical Analysis")
# Aquí pondrás RSI, MACD, etc.

st.header("💬 Social Media Sentiment")
# Aquí irán tweets, análisis y opción de resumir con IA

st.header("📰 News Summary")
# Aquí irán titulares + resumen IA

st.header("🤖 AI Summary / Recommendation")
# Aquí usas Ollama para resumir TODO lo anterior
