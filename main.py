from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from langchain_openai import ChatOpenAI
from tools.tools import tools
from langchain_core.runnables import RunnableConfig
load_dotenv(override=True)

# Step 1: Define the State object
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Step 2: Start the Graph Builder with this State class
graph_builder = StateGraph(State)
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools)

# Step 3: Create a Node
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=tools))

# Step 4: Create Edges
graph_builder.add_conditional_edges("chatbot", tools_condition, "tools")  # pyright: ignore
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# Step 5: Compile the Graph and Memory initialisation
db_path = "memory.db"
conn = sqlite3.connect(db_path, check_same_thread=False)
sql_memory = SqliteSaver(conn)

graph = graph_builder.compile(checkpointer=sql_memory)

# Config must be a RunnableConfig instance (dict with optional keys)
config: RunnableConfig = {
    "configurable": {
        "thread_id": "1",
        "checkpoint_ns": "default",
        "checkpoint_id": "1"
    }
}

def chat(user_input: str, history):
    result = graph.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config
    )
    return result["messages"][-1].content

gr.ChatInterface(chat, type="messages").launch()
