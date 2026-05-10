from fastmcp import FastMCP

mcp = FastMCP(name="calculator")

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    print(f"원격 MCP 서버: Multiplying {a} and {b}")
    return a * b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        path="/",
        log_level="debug",
    )
