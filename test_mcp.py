from mcp_instance import mcp
from tools import hello_world, debug_info
from prompts import test_prompt

print("MCP Instance:", mcp)
print("\nRegistered Tools:")
print(mcp.list_tools())
print("\nRegistered Prompts:")
print(mcp.list_prompts()) 