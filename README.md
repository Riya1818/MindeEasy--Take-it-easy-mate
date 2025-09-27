🧠 MindEase: AI-Powered Mental Health Companion
MindEase is an AI-powered chatbot designed to provide supportive, concise, and immediate initial guidance for users experiencing stress, anxiety, or feelings of being overwhelmed. It serves as a mental health companion, offering resources and coping strategies in a non-judgmental, structured format.
The application is built using a modern full-stack architecture, combining a high-performance Python FastAPI backend with a clean HTML/CSS/JavaScript frontend.

✨ Features
Gemini Integration: Uses the Google Gemini API (gemini-2.5-flash) for fast, context-aware conversational responses.

Conversational Memory: Utilizes LangChain's ConversationChain to maintain context across multiple turns for a fluid chat experience.

Document-Based RAG: Includes a /doc-chat endpoint powered by LlamaIndex for querying custom knowledge documents (e.g., mental health resources, FAQs).

Crisis Detection: Implements immediate keyword filtering (e.g., "suicidal", "kill myself") to detect potential crisis situations and provides a dedicated safety message with international helpline numbers.

Structured Output: AI responses are forced to be concise and empathetic, using numbered lists or short sentences for easy reading.

Modern UI/UX: Features a professional, soothing, two-column layout with color-coded chat bubbles and subtle UI enhancements (like smooth scrolling and button disabling).

🛠️ Technology Stack
Component	Technology	Purpose
Backend Framework	FastAPI	High-performance API server.
LLM Provider	Google Gemini API	Generative model for conversational responses.
LLM Frameworks	LangChain & LlamaIndex	Conversational memory, RAG, and core LLM chain logic.
Frontend	HTML5, CSS3, JavaScript	Simple, responsive chat interface.
Dependencies	python-dotenv, uvicorn	Environment variable management and ASGI server.

Export to Sheets
🚀 Getting Started
Follow these steps to set up and run the MindEase chatbot locally.

1. Prerequisites
You must have Python 3.9+ and a Gemini API Key.
Get a Gemini API Key: Obtain your key from Google AI Studio.
Create .env file: In the root of your project directory, create a file named .env and add your API key:
GEMINI_API_KEY="AIzaSy...[YOUR_GEMINI_API_KEY_HERE]"

2. Backend Setup (API & Logic)
Open your terminal in the project's root directory.

Create & Activate Virtual Environment (Recommended):
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Install Dependencies: Install all required packages. This list includes necessary Google and HuggingFace packages to avoid the old OpenAI dependencies.

pip install -r requirements.txt
Run the FastAPI Server: This starts the API backend on the port expected by the frontend.
uvicorn main:app --reload --host 0.0.0.0 --port 8000
The server is now running and waiting for requests at http://127.0.0.1:8000.

4. Frontend Execution (UI)
The frontend is a static web application and does not require a separate server.
Navigate to your project folder containing index.html.
Double-click index.html to open it in your web browser.
The frontend will automatically connect to the running FastAPI server.

💬 Use Cases
Role:	                Conversation:	                                                                             Backend Action:

Human	                I am feeling overwhelmed with work deadlines.	                                             Route: /chat endpoint.

AI	                  That sounds tough. Here are a few immediate steps:                              	         LLM: Gemini (via LangChain).
                      1. Prioritize: Focus only on the most critical task today.	
                      2. Take Breaks: Schedule 5-minute walks to reset your mind.	
                      3. Delegate: See if any small tasks can be shared or postponed.
