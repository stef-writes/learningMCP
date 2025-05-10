from mcp_instance import mcp
from mcp.server.fastmcp.prompts import base
from typing import List

@mcp.prompt()
def test_prompt(message: str) -> List[base.Message]:
    """
    A simple test prompt to verify MCP is working correctly.
    """
    return [
        base.SystemMessage("""
You are a helpful assistant that can use tools to help users.
You have access to:
1. hello_world() - A basic test tool
2. say_hello() - A test tool that uses OpenAI

Try both tools to verify everything is working.
"""),
        base.UserMessage(f"Please test the tools: {message}")
    ]

@mcp.prompt()
def quick_prompt(message: str) -> List[base.Message]:
    """
    Simple prompt for quick GPT-4 responses.
    """
    return [
        base.SystemMessage("""
You are a helpful assistant with access to GPT-4 through the quick_chat tool.
Use this tool to give very brief responses to the user's messages.
Keep everything concise.
"""),
        base.UserMessage(f"{message}")
    ]
