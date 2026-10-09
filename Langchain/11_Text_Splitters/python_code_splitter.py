# this is also a Recusive Character Text Splitter, but in this we will she how we can split codes
# so, we will have a programming language and Recursive Character Text Splitter will split the code on the basis of 
# class, functions, conditions..........

from operator import is_
from langchain_community.document_loaders.base_o365 import CHUNK_SIZE
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return self.name

    def is_passing(self):
        return self.grade >= 6.0


# Example usage
student1 = Student("Aviansh", 20, 8.2)

print(student1.get_details())

if student1.is_passing():
    print("The Student is passing")

else:
    print("The Student is not passing")

"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 150,
    chunk_overlap = 0,
)

#perform the split
chunk = splitter.split_text(text)

print(len(chunk))

for chunks in chunk:
    print(chunks)
    print("\n", "________________________________")