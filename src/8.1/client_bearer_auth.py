import asyncio
from fastmcp import Client

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZXYtdXNlciIsImlzcyI6Imh0dHBzOi8vY2FsYy5uZXRhZ2VyLmNvLmtyIiwiaWF0IjoxNzc4MzI4OTQwLCJleHAiOjE3ODA5MjA5NDAsImF1ZCI6ImNhbGN1bGF0b3IiLCJzY29wZSI6InJlYWQgd3JpdGUifQ.XyXmIT_LQqXFZI_IV_7sQQFpll7o_Ti3VEmrVVaJ8r9rynk5nFaosFqbIdBYBFHRT1i1OK3xw-Ov0mftwlFa3qdk09h4xvK8UI_oYQVLr4y9I6z4L_iaJjfx9pWcs8weUz-g3bDc7Gz9hcC6Umm4nMFwyQI_TV9-tFkscKx378HdN-sUisbZaeXIXP0ABxfmwgRf50nGXGVtE2-CqvYWHeFQZZGtfuar66A9RwLxIwmFZDvUfBoVijG-c9BlsMJU6yveulzihVpTDpKFATN1E9--ld5th7vkQF0y24W7LChLgIdwRkFfY_xY3hgqlEapv1-cXeGln_udwIyyxS13pw"
client = Client(
    "https://calc.netager.co.kr",
    auth=token,
)

async def main():
    async with client:
        print(f"Client connected: {client.is_connected()}")

        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        if any(tool.name == "multiply" for tool in tools):
            result = await client.call_tool("multiply", {"a": 3, "b": 7})
            print(f"multiply result: {result}")

    print(f"Client connected: {client.is_connected()}")

if __name__ == "__main__":
    asyncio.run(main())
