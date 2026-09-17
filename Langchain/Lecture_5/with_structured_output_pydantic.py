from typing import TypedDict, Annotated, Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

# schema
# this is our pydantic class

class Review(BaseModel):

    key_themes : list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summry : str = Field(description = "write down all the key themes discussed in the review")
    sentiment : Literal["pos", "neg"] = Field(description= "Return sentiment of the review" )
    pros : Optional[list[str]] = Field(default= None, description = "Write down all the pros inside a list")
    cons : Optional[list[str]] = Field(default= None, description = "Write down all the cons inside a list")
    name : Optional[str] = Field(default= None, description= "Write the name of the reviewer")



structured_model = model.with_structured_output(Review) # we have defined how the strucrure should be

result = structured_model.invoke("""recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:

Insanely powerful processor (great for gaming and productivity) Stunning 200MP camera with incredible zoom capabilities I

Long battery life with fast charging

5-Pen support is unique and useful

Cons:

Bulky and heavy-not great for one-handed use

Bloatware still exists in One UI

Expensive compared to competitors

Review by Avinash Kumar
""")

print(result)
# print(type(result)) # to see the data type of result
# print(result['name'])
#print(result.content[0]["text"]) 