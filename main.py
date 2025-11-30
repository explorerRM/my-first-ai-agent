# main.py
from agents.simple_agent import SimpleAgent
from tools.basic_tools import search_tool, calculator_tool

def main():
    # Create your first agent
    agent = SimpleAgent("Assistant")
    
    # Give it a task
    result = agent.think("Help me search for AI tutorials")
    print(result)
    
    # Use a tool
    search_result = search_tool("agentic AI tutorials")
    print(search_result)
    
    calc_result = calculator_tool("add", 5, 3)
    print(f"Calculator result: {calc_result}")

if __name__ == "__main__":
    main()
