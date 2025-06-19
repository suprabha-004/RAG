from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentence = "hello how are you"

embedding = model.encode(sentence)

print("embedding shape: ", embedding.shape)
print("embedding vector: ", embedding) 