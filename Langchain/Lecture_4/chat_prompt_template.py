# chat prompt template is used when we want System message and human message both to be dynamic
# e.g. System Message - you are a helpfull {domain} expert
#      Human Message - Explain me {topic}

# chat prompt template is same as prompt template = to create dynamic templates
# only difference is prompt template is used in single tern messages and chat prompt template is sued in multi tern template messages


from langchain_core.prompts import ChatPromptTemplate

# this thing don't work linke prompt template (prompt_ui_3.py). The formate is different form prompt template
# from langchain_core.messages import SystemMessage, HumanMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content = "You are a helpfull {domain} expert"),
#     HumanMessage(content = "Explain {topic} in simple terms" )
#     ]
# )

chat_template = ChatPromptTemplate([
    ('system','You are a helpfull {domain} expert'),
    ('human', 'Explain {topic} in simple terms')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic':'dusra'})

print(prompt)


