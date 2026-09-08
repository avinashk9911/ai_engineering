# In this code we will learn how to use external prmpt in Json formate (The Json file has beeb created by - prompt_generater.py file)

from langchain_core.prompts import PromptTemplate
from langchain_core.load import dumps # to save the prompt

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

#template.save(template.json) - this is not working because .json is deprecated
with open("Lecture_4/template.json", "w", encoding = "utf-8") as f: f.write(dumps(template))