# in this code we will see what RunnableLambda generates
from langchain_core.runnables import RunnableLambda

# I am creating a normal function whose work is to get a sentance and find the numbers of words in that word
def word_count(word):
    return len(word.split())

# converting this normal python function into Runnable
runnable_word_count = RunnableLambda(word_count)

print(runnable_word_count.invoke('Hello, How are you'))