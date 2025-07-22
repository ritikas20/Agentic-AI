import os
import json
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
import json
import os
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


llm=init_chat_model("groq:llama3-8b-8192")
search_tool = TavilySearchResults(k=5)

def search_node(state: dict):
    keyword = state.get("product")
    results = search_tool.invoke({"query": f"{keyword} product blog news"})
    text = "\n".join([res["content"] for res in results])
    return {**state, "search_results": text}

def summarize_node(state: dict):
    summary = llm.invoke(f"Summarize in 5 points:\n{state['search_results']}").content
    return {**state, "summary": summary}

def strategy_node(state: dict):
    prompt = f"Based on:\n{state['summary']}\nSuggest 3 market strategies."
    strategies = llm.invoke(prompt).content
    return {**state, "strategies": strategies}

def save_node(state: dict):
    filename = f"{state['product'].replace(' ', '_')}_report.json"
    with open(filename, "w") as f:
        json.dump({
            "product": state["product"],
            "summary": state["summary"],
            "strategies": state["strategies"]
        }, f, indent=2)
    return {**state, "file": filename}

def build_graph():
    builder = StateGraph(dict)
    builder.add_node("Search", search_node)
    builder.add_node("Summarize", summarize_node)
    builder.add_node("Strategy", strategy_node)
    builder.add_node("Save", save_node)

    builder.set_entry_point("Search")
    builder.add_edge("Search", "Summarize")
    builder.add_edge("Summarize", "Strategy")
    builder.add_edge("Strategy", "Save")
    builder.add_edge("Save", END)

    return builder.compile()
