import streamlit as st
import pandas as pd
import numpy as np

# Sidebar navigation
st.sidebar.title("📊 Dashboard Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Data", "Charts", "About"])

# Home Page
if page == "Home":
    st.title("🏠 Welcome to My Dashboard")
    st.write("This is a simple multi-page Streamlit app template.")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)

# Data Page
elif page == "Data":
    st.title("📂 Data Explorer")
    df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["Column A", "Column B", "Column C"]
    )
    st.write("Here’s a sample dataset:")
    st.dataframe(df)

# Charts Page
elif page == "Charts":
    st.title("📈 Charts & Visuals")
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )
    st.line_chart(df)
    st.bar_chart(df)

# About Page
elif page == "About":
    st.title("ℹ️ About This App")
    st.write("""
    This dashboard demonstrates:
    - Sidebar navigation
    - Multiple pages
    - Data display
    - Charts and visuals

    You can extend it with automation, metadata extraction, or any custom workflow.
    """)