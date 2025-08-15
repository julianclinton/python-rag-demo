from utils.loaders import load_pdf_files
from expandvars import expandvars
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings


# Load and prepare documents
print("📂 Loading PDF documents...")
docs = load_pdf_files(expandvars("$HOME/Documents/SPSSModeler/v18.5"))


splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)


print("🧠 Creating vector database...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embeddings)


retriever = db.as_retriever()
llm = OllamaLLM(model="mistral")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)


print("🤖 PDF Assistant ready. Type your question below. Type 'exit' to quit.")


# Chat loop
while True:
   query = input("\n📝 You: ")
   if query.lower() in ("exit", "quit"):
       print("👋 Bye! Take care.")
       break


   result = qa.invoke({"query": query})


   print("\n🤖 Assistant:\n", result["result"])


   print("\n📎 Sources:")
   for doc in result["source_documents"]:
       print(f" - {doc.metadata.get('source')}")
