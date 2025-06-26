import openai
import pandas as pd
import os

import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]


def run_query(prompt, df):
    # Convert a sample of the DataFrame to string for LLM context
    sample_data = df.head(20).to_csv(index=False)

    full_prompt = f"""You are a helpful data analyst. Analyze the following data and answer the user's question.

DATA SAMPLE:
{sample_data}

USER QUESTION:
{prompt}

Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful data analyst."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response['choices'][0]['message']['content']
