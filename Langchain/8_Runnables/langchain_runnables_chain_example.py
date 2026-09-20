# this code is the extension of langchain_runnables.py
# this is a example code for chains

# the task hear is that -> we need to create a application which will take a topic and pass it to a model for writing a jock on that, then
# we will pass that jock to model for explaning me that jock

import random
from abc import  ABC, abstractmethod

# we are creating a abstract class with a abstract function
class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass

#Component 1 - LLM
class nakli_llm(Runnable):
    def __init__(self):
        print("llm created")

    def invoke(self,input_data):
        response_list = [
            "Delhi is the capital of india",
            "AI stands for Arificial Intelligence",
            "IPL is a cricket league"
        ]

        return {'response': random.choice(response_list)}

# Component 2 - Prompt Template
class nakli_PromptTemplate(Runnable):
    def __init__(self, template, input_variable):
        self.template = template
        self.input_varianble = input_variable

    def invoke(self,input_dict):
        return self.template.format(**input_dict)

#Component3 - String output parser
class nakli_StrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self,input_data):
        return input_data['response']


        
#---------Now that we have standerised our components - we will connect them with chains
# the perpose of this call is to chain multiple components together
class Runnable_Connector(Runnable):

    def __init__(self, runnable_list): # this constructor will get the list of all the components
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data

# now it's time to use Runnable_connector
# 1st - we will create Prompt to generate jock
template1 = nakli_PromptTemplate(
    template = "write me jock on {topic}",
    input_variable= ['topic']
)

# 2nd prmpt to explain the jock
template2 = nakli_PromptTemplate(
    template = "Explain the following jock {response}",
    input_variable= ['response']
)

# 2nd - create a model
llm = nakli_llm()

# 3rd we meed a parser to print the final result
parser = nakli_StrOutputParser()


chain1 = Runnable_Connector([template1, llm])
# print(chain1.invoke({'topic':'AI'}))


chain2 = Runnable_Connector([template2, llm, parser])
# print(chain2.invoke({'jock':'This is a joke'}))

final_chain = Runnable_Connector([chain1,chain2])
print(final_chain.invoke({'topic': 'cricket'}))