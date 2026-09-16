from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

# schema

class Review(TypedDict):
    summry : str
    sentiment : str

structured_model = model.with_structured_output(Review) # we have defined how the strucrure should be

result = structured_model.invoke("""The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. 
Hopeing for a software update to fix this""")

print(result)
print(type(result)) # to see the data type of result
print(result['sentiment'])
#print(result.content[0]["text"])