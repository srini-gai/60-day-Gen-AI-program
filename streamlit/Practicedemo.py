import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ===================================================
# STREAMLIT CONFIG
# ===================================================
st.set_page_config(
    page_title="AI Stock Market Analysis Assistant",
    layout="wide"
)

st.title("📈 AI Stock Market Analysis Assistant")
st.caption("Reliable Market Data • Technical Analysis • AI Interpretation")

# ===================================================
# SIDEBAR
# ===================================================
st.sidebar.header("Stock Settings")

symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL").upper()
period = st.sidebar.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y"])

chart_type = st.sidebar.radio(
    "📊 Chart Type",
    ["Line Chart", "Candlestick Chart"]
)

analyze_btn = st.sidebar.button("🔍 Analyze Stock")

# ===================================================
# SAFE DATA DOWNLOAD
# ===================================================
@st.cache_data(show_spinner=False)
def load_stock(symbol, period):
    df = yf.download(
        tickers=symbol,
        period=period,
        auto_adjust=False,
        progress=False
    )

    if df.empty:
        return pd.DataFrame()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df.dropna(subset=["Close"], inplace=True)

    return df


# ===================================================
# INDICATORS
# ===================================================
def calculate_rsi(df, period=14):
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def calculate_macd(df):
    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()

    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    hist = macd - signal

    return macd, signal, hist


# ===================================================
# AI INTERPRETATION
# ===================================================
def ai_market_explanation(symbol, df):
    latest = df.iloc[-1]

    rsi = float(latest["RSI"])
    macd = float(latest["MACD"])
    close_price = float(latest["Close"])

    rsi_view = (
        "Overbought" if rsi > 70 else
        "Oversold" if rsi < 30 else
        "Neutral"
    )

    macd_view = "Bullish momentum" if macd > 0 else "Bearish momentum"

    return f"""
📊 AI Market Interpretation — {symbol}

• Current Price: {close_price:.2f}

• RSI ({rsi:.2f}): {rsi_view}

• MACD ({macd:.2f}): {macd_view}

📈 Trend Summary:
Market currently shows {macd_view.lower()} with RSI in a {rsi_view.lower()} zone.

⚠️ Disclaimer:
Educational purpose only — not financial advice.
"""


# ===================================================
# MAIN EXECUTION
# ===================================================
if analyze_btn:

    with st.spinner("Loading market data..."):
        df = load_stock(symbol, period)

    if df.empty or len(df) < 30:
        st.error("Not enough historical data available.")
        st.stop()

    # -------- calculate indicators --------
    df["RSI"] = calculate_rsi(df)
    df["MACD"], df["Signal"], df["Histogram"] = calculate_macd(df)

    df.dropna(inplace=True)

    # ===================================================
    # PRICE + MACD CHART
    # ===================================================
    st.subheader("📉 Price & MACD Chart")

    colors = np.where(df["Histogram"] >= 0, "#22c55e", "#ef4444")

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        row_heights=[0.7, 0.3]
    )

    # -------- PRICE SWITCH --------
    if chart_type == "Candlestick Chart":
        fig.add_trace(
            go.Candlestick(
                x=df.index,
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                name="Candlestick"
            ),
            row=1,
            col=1
        )
    else:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Close"],
                name="Close Price",
                line=dict(width=2)
            ),
            row=1,
            col=1
        )

    # -------- MACD --------
    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Histogram"],
            marker_color=colors,
            name="MACD Histogram"
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MACD"],
            name="MACD"
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Signal"],
            name="Signal"
        ),
        row=2,
        col=1
    )

    fig.update_layout(
        height=650,
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font=dict(color="white"),
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig, width="stretch")

    # ===================================================
    # TECHNICAL TABLE
    # ===================================================
    st.subheader("📊 Latest Technical Indicators")

    st.dataframe(
        df[["Close", "RSI", "MACD", "Signal"]].tail(10),
        width="stretch"
    )

    # ===================================================
    # AI ANALYSIS
    # ===================================================
    st.subheader("🧠 AI Market Analysis")

    st.text_area(
        "AI Explanation",
        ai_market_explanation(symbol, df),
        height=260
    )
