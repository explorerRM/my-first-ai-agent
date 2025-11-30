# agents/simple_agent.py
class SimpleAgent:
    def __init__(self, name):
        self.name = name
        self.memory = []
    
    def think(self, task):
        """Agent processes the task"""
        print(f"{self.name} is thinking about: {task}")
        self.memory.append(task)
        return f"I will help you with: {task}"
    
    def use_tool(self, tool_name, *args):
        """Agent can use tools"""
        print(f"{self.name} is using tool: {tool_name}")
        return f"Tool {tool_name} executed"
