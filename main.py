# code for main.py for dummy tool

from agent import AutoAgent
from tools.search_tool import search_tool
from tools.code_tool import code_tool

if __name__ == "__main__":
    agent = AutoAgent()
    agent.register_tool("search", search_tool)
    agent.register_tool("code", code_tool)
    
    agent.run("Research on AI Agents and run a Python code to print 1-5 squared.")