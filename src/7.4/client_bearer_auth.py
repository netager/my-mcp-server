import asyncio
from fastmcp import Client

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZXYtdXNlciIsImlzcyI6Imh0dHBzOi8vZGV2LmV4YW1wbGUuY29tIiwiaWF0IjoxNzc4MzE5NjM1LCJleHAiOjE3ODA5MTE2MzUsImF1ZCI6ImNhbGN1bGF0b3IiLCJzY29wZSI6InJlYWQgd3JpdGUifQ.kE1kQpKJqDZo8NmfoqOKZ0C5BqAFHaOieWa2eggGYfok3NPCbw0d1G5T-I68iSGjVMhgShOqhrybek4341VQWXvME9L0yEAawusr8jb7S166Hm5XER0cmZJ81v7-BOS1hurQDfqbonRvyhTk1UfE5o2dxUl2_IL_uQL6sOWso6DeufurW_RLNTUDuvyFDZZ6KxSc8JUNu5Cn1htXcphy6InzBphFj68zXh6v7r1-nyBPyKdGtnVqFPRlD3Fma_xYspj4WZSh4drltNEztxgoTUyx5-cnQoPAnRznaytHFlQqNSk4VkKYKzj2ziRExRQj-WO4L08GGBuOPdZkpfvIsw"
client = Client(
    "http://localhost:8000",
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
