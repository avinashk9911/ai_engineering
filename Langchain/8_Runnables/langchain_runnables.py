# now with the hlep of runnables we can standerize the components (e.g. llm, promptTemplate)

# to standerize components we are creating two compoents 1) LLM 2)PromptTemplate
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

    # we won't remove this code just becasue for some users who has developed thear application using this method migt get trable
    # def predict(self, prompt):

    #     response_list = [
    #         "Delhi is the capital of india",
    #         "AI stands for Arificial Intelligence",
    #         "IPL is a cricket league"
    #     ]

    #     return {'response': random.choice(response_list)}

# Component 2 - Prompt Template
class nakli_PromptTemplate(Runnable):
    def __init__(self, template, input_variable):
        self.template = template
        self.input_varianble = input_variable

    def invoke(self,input_dict):
        return self.template.format(**input_dict)

    # we won't remove this code just becasue for some users who has developed thear application using this method migt get trable
    # def format(self, input_dict):
    #     return self.template.format(**input_dict)


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
# 1st - we will create Prompt
template = nakli_PromptTemplate(
    template = "write me a {length} poem about {topic}",
    input_variable= ['length','topic']
)

# 2nd - create a model
llm = nakli_llm()

# 3rd create chain
chain = Runnable_Connector([template, llm])

print(chain.invoke({'length':'Long','topic':'India'}))
        

# now we can create a component3 and add that too in the same chain
parser = nakli_StrOutputParser()

chain_1 = Runnable_Connector([template, llm, parser])
print(chain_1.invoke({'length':'Long','topic':'India'}))
