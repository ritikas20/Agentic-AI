# 🧠 Agentic AI: Market Research Assistant with LangGraph

This project demonstrates an **agentic AI system** using [LangGraph](https://github.com/langchain-ai/langgraph) to perform autonomous market research. Given a product name, the system:

1. Searches the internet for recent blog/news content (via Tavily).
2. Summarizes key insights using GPT-4.
3. Recommends go-to-market strategies.
4. Saves everything in a structured report.

---

## 📦 Tech Stack

- **[LangGraph](https://github.com/langchain-ai/langgraph)** – for building the multi-step agent graph
- **[LangChain](https://www.langchain.com/)** – to manage LLM calls and tools
- **[Tavily Search API](https://app.tavily.com/)** – for real-time search results
- **[OpenAI GPT-4](https://platform.openai.com/)** – for summarization and strategy generation
- **Python 3.9+**

<img width="670" height="289" alt="image" src="https://github.com/user-attachments/assets/5748520b-e234-43f3-9de4-8efcff8cae48" />

## 🚀 Setup Instructions
```bash
### 1. Clone the repo


git clone https://github.com/your-username/Agentic-AI
cd Agentic-AI

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add API keys
Create a .env file:

OPENAI_API_KEY=your-openai-key
TAVILY_API_KEY=your-tavily-key

### 4. Run the code in terminal
python app1.py
```bash







