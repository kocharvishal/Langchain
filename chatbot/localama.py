from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Set LangChain environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")

# Initialize Ollama model
try:
    llm = Ollama(model='llama3.2')
except Exception as e:
    st.error(f"Failed to initialize Ollama: {str(e)}")
    st.stop()

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond in a friendly and informative manner."),
        ("user", "Question: {question}")
    ]
)

# Create chain
chain = prompt | llm | StrOutputParser()

# Streamlit UI
st.title("Chatbot with Localama")
input_text = st.text_input("Enter your question:")

if input_text:
    with st.spinner('Generating response...'):
        try:
            response = chain.invoke({"question": input_text})
            st.write(response)
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")