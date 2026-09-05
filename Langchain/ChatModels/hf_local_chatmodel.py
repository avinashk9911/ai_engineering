#this example shows how to locally run a model using the HuggingFacePipeline and 
# ChatHuggingFace classes from the langchain_huggingface package. 
# It loads a specific model, sets up the pipeline with desired parameters, and 
# then invokes the model with a query.

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(temperature=0.5, max_length=100)
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the prime minister of India?")

print(result)