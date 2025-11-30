# tools/basic_tools.py
def search_tool(query):
    """Simulates a search tool"""
    return f"Search results for: {query}"

def calculator_tool(operation, a, b):
    """Simple calculator"""
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    return "Unknown operation"
