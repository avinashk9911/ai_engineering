# we are creating a fack llm

import random

# this is a dummy llm that we have created
class nakli_llm:
    def __init__(self):
        print("llm created")

    def predict(self, prompt):

        response_list = [
            "Delhi is the capital of india",
            "AI stands for Arificial Intelligence",
            "IPL is a cricket league"
        ]

        return {'response': random.choice(response_list)}  # we are returning dictionary because in actual llm output we also get dictionary,and to access our actual response we do result.response

# to test this nakli_llm we can do ->
# llm = NakliLLM()
# llm.predict("what is the capital of India") #oviouly it is a dummy llm so it will just give a random output form the response_list.

# this is the dummy prompt template that we are creating
class nakli_PromptTemplate:
    def __init__(self, template, input_variable):
        self.template = template
        self.input_varianble = input_variable

    def format(self, input_dict):
        return self.template.format(**input_dict)

# to test this nakli_PromptTemplate
template_test = nakli_PromptTemplate(
    template = "write me a {length} poem about {topic}",
    input_variable= ['length','topic']
)
#print(template_test.format({'length':'sort','topic':'india'}))

#--------------Till now we have created two components 1)nakli_llm and 2)nakli_PromptTemplate
# now as a AI engineer I want create llm application which -> will take input form user and generate output

# 1st we need a prompt
template = nakli_PromptTemplate(
    template = "write me a {length} poem about {topic}",
    input_variable= ['length','topic']
)

prompt = template.format({'length': 'Sort', 'topic': 'India'})

# 2nd we will need a llm
llm = nakli_llm()

# 3rd we will pass prompt into llm and then print the response
result = llm.predict(prompt)
print(result['response'])


#--------------till now you have seen how manually we use two components seperatily with there own expra working
# now we will create chain so, that we can reduct some extra efforts

class nakli_chian:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict): #this will take a input data (e.g.{'length': 'Sort', 'topic': 'India'} ) in a dictionary format
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']  #this is becasue we know llm will return a dictionary and we in chains we just return actual response

# -----now to test this chain

# 1st a prompt
template_chain = nakli_PromptTemplate(
    template = "write me a {length} poem on {topic}",
    input_variable= ['sort','India']
)

# prompt = template_chain.format(template_chain) #in chains we don't have to do this part

# 2nd a model
llm_chain = nakli_llm()
# result = llm_chain(prompt) # in chains we don't have to do this

#3d chain
#chain(llm,prompt)
chain = nakli_chian(llm,template_chain)

print(chain.run({'length':'sort', 'topic':'India'}))

# with the help of chain we don't have to fomat templte and nore we have to predict llm.



