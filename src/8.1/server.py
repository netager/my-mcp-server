from fastmcp import FastMCP
# from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.jwt import JWTVerifier

public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtQW205UGONSK3jx47vaZ
toZrTptGqZH7Hch1OBU6d7pYsQ2w1/wehCB9588WMnRMJ0VJRyoQIUrDZAFEPOJQ
ZW5OFg2jBUBEgQpuIXuB3V/r1nbpOPyVivT5KLdWD/nDyB565P3HYCQA6sEnISyj
tk9jaHsk9ZuX9f1TBv4rKUjG4XZW6rZutv++3zufF94V8JKVEvytroplpkLsKbLL
Ry/gIcZey5s7fDbQhRZDFO7KqgDv7wLMMc0Wz3GAGtZ9Ari9Czlgn6QMmbudHNFb
jrLpMI39onk3n7yvpbAQPG0yGZ4MdjGhV85ELlj7ppDbGHZYQjBWTleetAx/2XYd
oQIDAQAB
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