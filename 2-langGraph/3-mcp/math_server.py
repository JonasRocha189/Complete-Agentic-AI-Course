from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """_summary_: Adds two numbers together"""
    return a + b
  
  
@mcp.tool()
def multiply(a:int, b:int) -> int:
    """_summary_: Multiplies two numbers together"""
    return a * b
  
# The transport='stdio' argument tells the server to communicate with the client over standard input/output.
# Use Standard I/O (stdin and stdout) transport to receive and respond to tool function calls.
if __name__ == "__main__":
    mcp.run(transport="stdio")