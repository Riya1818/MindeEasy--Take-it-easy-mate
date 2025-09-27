import os
import dotenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
# NEW: Import PromptTemplate and ConversationBufferMemory
from langchain.prompts import PromptTemplate 

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API_KEY, temperature=0.6) # Slightly lower temperature for consistency

# --- NEW: Custom Prompt Template for Concise, Structured Output ---
# This prompt guides the AI to be brief and use bullet points, avoiding long paragraphs.
CUSTOM_PROMPT = """You are MindEase, a supportive and brief mental health companion.
Your responses MUST be concise, empathetic, and structured using bullet points or numbered lists.
Do not use long paragraphs. Keep the output easy to read and focus on 3-4 key points.
Do not use markdown formatting like ** or ## inside the response body itself.

Current conversation:
{history}
Human: {input}
AI:"""

PROMPT = PromptTemplate(input_variables=["history", "input"], template=CUSTOM_PROMPT)
# --------------------------------------------------------------------

#store per-user memory sessions
session_memory_map = {}

def get_response(session_id : str, user_query: str) -> str:
    if session_id not in session_memory_map:
        memory = ConversationBufferMemory()
        # NEW: Pass the custom prompt into the ConversationChain
        session_memory_map[session_id] = ConversationChain(
            llm=llm, 
            memory=memory, 
            prompt=PROMPT, # Add the new prompt here
            verbose=True
        )

    conversation = session_memory_map[session_id]
    return conversation.predict(input=user_query)