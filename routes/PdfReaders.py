from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

reader = PdfReader("Booking-Conditions.pdf")

texts = ""

# Extract text from PDF

for page in reader.pages:

    extracted = page.extract_text()

    if extracted:

        texts += extracted

# Split into chunks

splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50

)

chunks = splitter.split_text(texts)

print("Total chunks:", len(chunks))

# Create embeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma.from_texts(texts=chunks, embedding=embeddings)

data = db.get(include=["embeddings"])

print(data["embeddings"][0][:10])

# Similarity search

results = db.similarity_search("What is Avis cancellation policy?", k=3)

context = "\n\n".join([r.page_content for r in results])

print(context)


