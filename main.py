# code for main.py for dummy tool
from agent import AutoAgent
from tools.search_tool import search_tool

if __name__ == "__main__":
    agent = AutoAgent()
    agent.register_tool("search", search_tool)
    agent.run("Research latest on AI agents")
