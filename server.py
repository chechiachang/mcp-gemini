import os
import json
from dotenv import find_dotenv
from dotenv import load_dotenv
from fastmcp import Client
import asyncio
from fastmcp.client.transports import StdioTransport

async def main():
    load_dotenv(find_dotenv(), override=True)
    
    transport=StdioTransport(
        command="uvx",
        args=["--from", "git+https://github.com/narumiruna/yfinance-mcp", "yfmcp"],
    )
    client = Client(transport=transport)

    async with client:
        await client.ping()
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()
        for tool in tools:
          print(f"Tool: {tool.name}")
          print(f"Description: {tool.description}")
          if tool.inputSchema:
              print(f"Parameters: {tool.inputSchema}")
          # Access tags and other metadata
          if hasattr(tool, '_meta') and tool._meta:
              fastmcp_meta = tool._meta.get('_fastmcp', {})
              print(f"Tags: {fastmcp_meta.get('tags', [])}")

asyncio.run(main())
