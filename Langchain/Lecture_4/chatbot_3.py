# this is a code to show how we can sotore the converstion.
# this is importent becasue - if we dont lable the coverstation and the conversation gets bigger the Bot won't
# be able to distinguse between it's own message and user message
# another exaple is messages.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

chat_history = [SystemMessage(content = "You are helpful AI assistant")] #this list will store all the prevous chat for bot to reffer.

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content = user_input)) # adding user input
    if user_input == "exit":
        break
    result = model.invoke(chat_history) # passing entire list of conversation
    chat_history.append(AIMessage(content = result.content[0]["text"])) # adding the response of the AI
    print("AI : ",result.content[0]["text"]) #print response

print(chat_history) # to see the entire conversation'