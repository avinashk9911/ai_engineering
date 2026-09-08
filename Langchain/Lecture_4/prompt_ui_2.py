# in this code we have learned how to use Prompt template. This kind of prompt templates are called
# Dynamic Prompts.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

st.header('Research tool')

paper_input = st.selectbox("Select Research Paper Name",["Select.......", "Attention is All you need", "BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: lANGUAGE mODELS ARE Few-Short Learning", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style",["Bigneer-Friendly","Technical", "Code-Oriented" "Mathematical"])

length_input = st.selectbox("Select Explanation Style", ["Short (1-2 paragraphs)", "Medium (3-5 paragrpahs)","Long (Detailed Explanation)"])

#template
template = PromptTemplate(template = """
Please summarie the research paper titled "{paper_input}" with the following specifications:
Eplanation Style : {style_input}
Eplanation Length : {length_input}

1. Methematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
- use relatable analogies to simpligy comple ideas.

If certain information is not available in the paper, respond with - "Insufficient information available" instead of guessing

Ensure the summary is cleaer accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input', 'length_input'],
validation_template = True #this will check if we have done anything wrong in input_variales
)

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