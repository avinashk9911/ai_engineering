# in this code we are learning about Recursive Character Text Splitter -> thorough this splitting technique
# we can split on the basis of paragraph, line break, spaces/words, and each alphabet.
# this spletting depends upon chunk size -> if the size is big I can split on the basis of paragraph and if very
# small we can break on the basis of words or alphabets.

# benafit of using Recursive Character Text Splitter is that -> this split doesn't splits in between words.
# it tries to keep words intact

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what's possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

# initalize the splitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0,
)

# perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print("\n")
print(chunks)
print("\n")
for i in chunks:
    print(i)
    print("\n")