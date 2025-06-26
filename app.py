import streamlit as st
import pandas as pd
from query_engine import run_query

st.set_page_config(page_title="GenAI Sales Analyst", layout="wide")
st.title("📊 AI-Powered Sales Analyst")

try:
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        st.success("File uploaded!")

        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())  # Show first 5 rows

        user_input = st.text_input("Ask your question about the data 👇")

        if user_input:
            with st.spinner("Thinking..."):
                try:
                    response = run_query(user_input, df)
                    st.markdown("### 🤖 AI Response")
                    st.write(response)
                except Exception as e:
                    st.error(f"❌ Error during query: {e}")
except Exception as app_error:
    st.error(f"❌ App failed: {app_error}")
