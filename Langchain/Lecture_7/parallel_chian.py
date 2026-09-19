# In this code we will learn about parallel chains
# to understand ||el chian we take a example -
# lets say we have a detailed report on linear rigration, now on this we will provide users with combined notes and quiz.
# now to acchieve this we will need ||el chain

# the architecture for this will be - form one document we will call model1 to generate notes, model2 to generate quiz and then finally model3 to combine both output and create the final result.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

#model1 - google/gemma-2-2b-it
llm1 = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    # max_new_tokens=256,
)

# model2 - meta-llama/Llama-3.2-1B-Instruct
llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="conversational",
    provider="featherless-ai",  # TinyLlama is not on the default "auto" provider
    # max_new_tokens=256,
)

model1 = ChatHuggingFace(llm = llm1)
model2 = ChatHuggingFace(llm = llm2)

#prompt1 - to generate summary
prompt1 = PromptTemplate(
    template= 'Generate short and simple notes form the following text \n {text}',
    input_variable = ['text']
)

#prompt2 - to generate quiz
prompt2 = PromptTemplate(
    template= "Generate 5 question and answer for the following text \n {text}",
    input_variables=['text']
)

#prompt3 
prompt3 = PromptTemplate(
    template= 'Merge the provided notes and quiz into single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables= ['notes','quiz']
)

#parser
parser = StrOutputParser()

# we are going to use chains in two parts 1st for ||el models i.e. notes and quiz and 2nd will be to merge both
#1st -> ||el chain - to generate notes and quize
parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})
#2nd -> chain to generate merged result
merge_chain = prompt3 | model1 | parser

# now we will combined both the chains to work together and generate final result
chain = parallel_chain | merge_chain

text = """ 
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({'text' : text})

print(result)

# to visualize the chain
chain.get_graph().print_ascii()


