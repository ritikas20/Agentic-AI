# 🤖 Agentic AI Market Research Bot (LLaMA3 + LangGraph + Flask)

This project demonstrates a **multi-step autonomous agent** built using [LangGraph](https://github.com/langchain-ai/langgraph), [Groq's LLaMA3 8B](https://console.groq.com/), and [Tavily](https://www.tavily.com/) search API.  
It powers a Flask web app that performs real-time market research based on user queries.

Ask:
"What are the current trends for electric toothbrushes?"
"Give me 3 marketing strategies for it."
"How can we make it work for Indian customers?"

The bot:

Uses the web (via Tavily) to search

Summarizes trends using 

Suggests strategy

Remembers your previous inputs

---


## 🚀 Setup Instructions
```bash
## 1. Clone the repo


git clone https://github.com/your-username/Agentic-AI
cd Agentic-AI

## 2. Install dependencies

pip install -r requirements.txt

## 3. Add API keys
Create a .env file:

OPENAI_API_KEY=your-openai-key
TAVILY_API_KEY=your-tavily-key

## 4. Run the code in terminal
python app1.py








