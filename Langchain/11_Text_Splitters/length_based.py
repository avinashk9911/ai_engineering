from langchain_text_splitters import CharacterTextSplitter

text = """
The Times of India (TOI) is an Indian English-language daily news and digital news media outlet. It is the third-largest newspaper in India by circulation and the ninth-largest selling English-language daily in the world. It is the oldest English-language newspaper in India and the second-oldest Indian newspaper still in circulation, with its first edition published in 1838. It is nicknamed "The Old Lady of Bori Bunder". It is considered a newspaper of record. Near the beginning of the 20th century, Lord Curzon, the Viceroy of India, called TOI "the leading paper in Asia". In 1991, the BBC ranked TOI among the world's six best newspapers. It is owned and published by Bennett, Coleman & Co. Ltd. (BCCL), which is controlled by the Sahu Jain family. In the Brand Trust Report India study 2019, TOI was rated as the most trusted English newspaper in India. In a 2021 survey, the Reuters Institute for the Study of Journalism rated TOI the most trusted news brand among English-speaking online news users in India. Since the 2000s, the newspaper has also been criticised for establishing the practice of accepting payments in exchange for positive coverage in the Indian news industry.

"""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_text(text)
print(result)