# this is a fully functional chatbot whichhave the context of the conversation

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

chat_history = [] #this list will store all the prevous chat for bot to reffer.

while True:
    user_input = input("You : ")
    chat_history.append(user_input) # adding user input
    if user_input == "exit":
        break
    result = model.invoke(chat_history) # passing entire list of conversation
    chat_history.append(result.content[0]["text"]) # adding the response of the AI
    print("AI : ",result.content[0]["text"]) #print response

print(chat_history) # to see the entire conversation'