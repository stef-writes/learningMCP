from mcp_instance import mcp
import os
from dotenv import load_dotenv
import sys
import platform
from json_logger import log_interaction # Import the logger

# Load environment variables
load_dotenv()

@mcp.tool()
def hello_world() -> str:
    """A simple test tool to check if MCP is working."""
    tool_name = "hello_world"
    inputs = {}
    output = None
    error = None
    try:
        output = "Hello from MCP! Everything is working."
        return output
    except Exception as e:
        error = str(e)
        return f"Error in {tool_name}: {error}"
    finally:
        log_interaction(tool_name, inputs, output, error)

@mcp.tool()
def debug_info() -> str:
    """Get debug information about the environment."""
    tool_name = "debug_info"
    inputs = {}
    output = None
    error = None
    try:
        # Check if API keys are set (showing only first few chars for security)
        openai_key = os.getenv("OPENAI_API_KEY", "Not set")
        
        if openai_key != "Not set" and len(openai_key) > 9:
            openai_key = openai_key[:5] + "..." + openai_key[-4:]
        
        info = {
            "python_version": sys.version,
            "platform": platform.platform(),
            "openai_key": openai_key,
            "pwd": os.getcwd(),
            "files_in_dir": os.listdir(".")[:10]  # First 10 files
        }
        output = str(info)
        return output
    except Exception as e:
        error = str(e)
        return f"Error in {tool_name}: {error}"
    finally:
        log_interaction(tool_name, inputs, output, error) 