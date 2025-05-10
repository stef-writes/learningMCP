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
For this test, you can use the hello_world() tool to verify everything is working.
"""),
        base.UserMessage(f"Please help me with this: {message}")
    ]
