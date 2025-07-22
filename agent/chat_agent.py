from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


llm=init_chat_model("groq:llama3-8b-8192")

def init_memory(history):
    memory = ConversationBufferMemory()
    for i in range(0, len(history), 2):
        human, user_msg = history[i]
        ai, ai_msg = history[i+1]
        memory.chat_memory.add_user_message(user_msg)
        memory.chat_memory.add_ai_message(ai_msg)
    return memory

def get_response(message, memory):
    chain = ConversationChain(llm=llm, memory=memory)
    return chain.run(message)
