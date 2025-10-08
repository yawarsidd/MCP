# math_server.py
from mcp.server.fastmcp import FastMCP
import logging

# Silence verbose request logs
logging.getLogger("mcp.server").setLevel(logging.WARNING)

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")