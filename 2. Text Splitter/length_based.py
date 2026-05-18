from langchain_text_splitters import CharacterTextSplitter

text = """Cricket is one of the most popular sports in the world, especially in countries like India, Australia, and England. It is played between two teams of eleven players on a large oval field with a rectangular pitch at the center. The main objective of the game is to score more runs than the opposing team by batting and running between wickets or hitting boundaries. Cricket has three major formats: Test matches, One Day Internationals, and T20, each offering a unique style of play. The sport requires teamwork, strategy, patience, and skill, making it both exciting to play and enjoyable to watch for millions of fans.
"""

# Fix: Changed 'splitter' to 'separator'
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator='' 
)

result = splitter.split_text(text)

for i, chunk in enumerate(result):
    print(f"Chunk {i+1}: {chunk}\n")