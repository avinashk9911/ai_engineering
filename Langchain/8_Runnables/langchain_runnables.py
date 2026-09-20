# now with the hlep of runnables we can standerize the components (e.g. llm, promptTemplate)

# to standerize components we are creating two compoents 1) LLM 2)PromptTemplate
import random

class nakli_llm:
    def __init__(self):
        print("llm created")

    def predict(self, prompt):

        response_list = [
            "Delhi is the capital of india",
            "AI stands for Arificial Intelligence",
            "IPL is a cricket league"
        ]

        return {'response': random.choice(response_list)}

class nakli_PromptTemplate:
    def __init__(self, template, input_variable):
        self.template = template
        self.input_varianble = input_variable

    def format(self, input_dict):
        return self.template.format(**input_dict)
