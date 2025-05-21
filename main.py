import streamlit as st
import openai
import os

st.title("Meeting Summary Generator")

openai.api_key = os.getenv("OPENAI_API_KEY")

transcript = st.text_area("Paste meeting transcript (.txt content)")

if transcript:
    prompt = f"Summarize the following meeting transcript and list action items:\n\n{transcript}"
    with st.spinner("Summarizing..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success(response.choices[0].message["content"])
