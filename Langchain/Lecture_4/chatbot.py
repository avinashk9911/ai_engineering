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