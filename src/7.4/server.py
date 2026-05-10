from fastmcp import FastMCP
# from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.jwt import JWTVerifier

public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwU4znICQ+4huSyX57P4k
l2XWs5ydWkt0hooxeGmHqQU1U6cb4y/2Bk1RPvLN4qUHWAGlfYw4mk2LM9gzxqJM
Hz8BexRLv7PyNMJ728+Mfj147C76sKg+qQ9buJY1GgDmhg6l1zUiuXo7kMhv5UtY
VRoVBaWaSJdVhcxMXIXNVB6NLAFMCQcAQ94mbKqbD9v5A/NJxoHA/BGzklTdBT+Z
hLM02jULecFZ5ir4FjoytWgFt1/RN0FhjG+GlL4tbVXCLhBCFEakA7m2OcTCk/ST
K7EYK3XU8zTyh+e9pvM7gf9WohFBXEEB4KdSLMhXXpXvHjhiw6ef1wMq7JiOnKhF
hwIDAQAB
-----END PUBLIC KEY-----"""

auth = JWTVerifier(
    public_key=public_key,
    issuer="https://dev.example.com",
    audience="calculator"
)

mcp = FastMCP(name="calculator", auth=auth)

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    print(f"원격 MCP HTTP 서버: Multiplying {a} and {b}")
    return a * b


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        path="/",
        log_level="debug"
    )