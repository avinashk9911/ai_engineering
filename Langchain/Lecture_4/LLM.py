# Local test of a small instruct LLM with LangChain.
# HuggingFaceTB/SmolLM-360M-Instruct is downloaded once, then run on your machine.
# Flow: prompt -> ChatHuggingFace (applies chat template) -> HuggingFacePipeline -> generated text

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceTB/SmolLM-360M-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=80,
        temperature=0.3,
        do_sample=True,
        return_full_text=False,
    ),
)

model = ChatHuggingFace(llm=llm)

prompt = "Explain me about attantion all you need paper in 5 lines"
print("Prompt:", prompt)

result = model.invoke(prompt)

print("\n--- Model output ---")
print(result.content)
