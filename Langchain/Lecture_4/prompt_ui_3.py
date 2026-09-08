# in this code we wil learn how to use external prompt template i.e template.json

from pathlib import Path

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.load import loads

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

st.header('Research tool')

paper_input = st.selectbox("Select Research Paper Name",["Select.......", "Attention is All you need", "BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: lANGUAGE mODELS ARE Few-Short Learning", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style",["Bigneer-Friendly","Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragrpahs)","Long (Detailed Explanation)"])

# calling external template (saved by prompt_generator.py via dumps)
template_path = Path(__file__).parent / "template.json"
with template_path.open(encoding="utf-8") as f:
    template = loads(f.read())

#fill the placeholders
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input' : length_input
})

if st.button("Generate"):
    result = model.invoke(prompt)
    #st.write(result.content)
    st.write(result.content[0]["text"])