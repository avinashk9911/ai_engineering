# This a simple chatbot withoud conversation context i.e this bot won't have the chat history, SO
# we can't ask somthing related to the previous chat.
# e.g.:
# AI :  The sum of 2 and 0 is **2**.
# You : multiply this with 10
# AI :  It looks like you didn't include the number or problem! Please provide what you would like me to multiply by 10, and I'll give you the answer.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI : ",result.content[0]["text"])