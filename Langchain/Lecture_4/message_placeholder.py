# message place holder is a place holder where we create a placeholder for set of messages.
# generally this is used to retrive or store chat history

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
    ('system', 'you are a helpfull customer support agnet'),
    MessagesPlaceholder(variable_name='chat_history'),# this is the place where all the previous chat history will comup. So that the model will have the context of prevous chat
    ('human', '{query}')
])

# load chat history

chat_history = []

with open("Langchain/Lecture_4/chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)
print()

# hreate prompt
# chat_template.invoke({'chat_history':chat_history, 'query':HumanMessage(content= 'Where is my refund')}) we don't have to define HumanMessage because in Line 8 we have difined we this will be a humanmessage
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})
print(prompt)


