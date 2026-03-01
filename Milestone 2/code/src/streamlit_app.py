import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Python → Java Translator", layout="wide")
st.title("Python → Java Translator (Gemini 3 Flash)")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY not found. Add it in Settings → Secrets.")
    st.stop()

client = genai.Client(api_key=API_KEY)

python_code = st.text_area("Enter Python Code", height=250)

if st.button("Translate"):
    if not python_code.strip():
        st.warning("Please enter Python code.")
    else:
        prompt = f"""
You are an expert software engineer.
Translate the following Python code into clean, modern Java.
Only output the Java code.

Python Code:
{python_code}

Java Code:
"""
        with st.spinner("Generating..."):
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
            )

        st.subheader("Generated Java Code")
        st.code(response.text, language="java")