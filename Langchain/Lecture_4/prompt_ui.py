# from langchain_google_genai import ChatGoogleGenerativeAI
#from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

st.header('Research tool')

user_input = st.text_input("Enter your prompt")

if st.button("Generate"):
    result = model.invoke(user_input)
    st.write(result.text)