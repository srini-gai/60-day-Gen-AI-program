import streamlit as st
import pandas as pd

st.title("📈 Dixon Stock Dashboard")

uploaded_file = st.file_uploader("Upload Dixon stock Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Convert Excel serial dates to proper datetime
    if not pd.api.types.is_datetime64_any_dtype(df['Date']):
        df['Date'] = pd.to_datetime(df['Date'], origin='1899-12-30', unit='D')

    st.subheader("📂 Raw Data")
    st.dataframe(df)

    st.subheader("📊 Summary Statistics")
    st.dataframe(df[['Close','Open','High','Low']].agg(['mean','min','max']).T)

    st.subheader("📉 Close vs Open Prices")
    st.line_chart(df.set_index("Date")[["Close","Open"]])

    st.subheader("📊 High vs Low Prices")
    st.line_chart(df.set_index("Date")[["High","Low"]])