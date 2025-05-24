import requests
import streamlit as st

def get_ollama_response(input_text):
    response= requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input':{"topic": input_text}}
    )
    return response.json()['output']['content']
#streamlit UI
st.title("Essay Generator with Ollama")
input_text = st.text_input("Enter the topic for your essay:")

if input_text:
    st.write(get_ollama_response(input_text))