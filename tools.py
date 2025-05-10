from mcp_instance import mcp
import os
from dotenv import load_dotenv
import sys
import platform

# Load environment variables
load_dotenv()

@mcp.tool()
def hello_world() -> str:
    """A simple test tool to check if MCP is working."""
    return "Hello from MCP! Everything is working."

@mcp.tool()
def debug_info() -> str:
    """Get debug information about the environment."""
    # Check if API keys are set (showing only first few chars for security)
    openai_key = os.getenv("OPENAI_API_KEY", "Not set")
    
    if openai_key != "Not set":
        openai_key = openai_key[:5] + "..." + openai_key[-4:]
    
    info = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "openai_key": openai_key,
        "pwd": os.getcwd(),
        "files_in_dir": os.listdir(".")[:10]  # First 10 files
    }
    
    return str(info) 