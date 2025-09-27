import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings # NEW: Import Settings
from llama_index.llms.google_genai import GoogleGenAI # Use GoogleGenAI
# from llama_index.llms.gemini import Gemini as LlamaGemini # OLD/Alternative import
# from llama_index.llms.google_genai import GoogleGenAI as LlamaGemini # Previous suggestion's import

# Load the key from environment variables for explicit use
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    # This check is crucial, although it should be handled in chat_engine/main
    pass 

# Initialize the LLM explicitly
llama_llm = GoogleGenAI(model="gemini-2.5-flash", api_key=GEMINI_API_KEY)


Settings.llm = llama_llm

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")


documents = SimpleDirectoryReader("data").load_data( )

index = VectorStoreIndex.from_documents(documents) 

query_engine = index.as_query_engine(llm = llama_llm)

def query_documents(user_query: str) -> str:
    return str(query_engine.query(user_query))