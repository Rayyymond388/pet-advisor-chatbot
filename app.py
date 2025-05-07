import streamlit as st
import openai
import os
from dotenv import load_dotenv

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🐾 Pet Advisor Chatbot")

user_input = st.text_input("Ask me about your pet:")

if user_input:
    messages = [
        {"role": "system", "content": "You are a friendly pet advisor who gives helpful and safe advice about pets."},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    st.write("🐶 Pet Advisor:", response.choices[0].message.content)
