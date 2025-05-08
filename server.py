from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your modules
from tools import *
from resources import *
from prompts import *

# Initialize FastMCP with a name
mcp = FastMCP("Demo")

# Register your tools, resources, and prompts
# These will be automatically registered from the imported modules

if __name__ == "__main__":
    mcp.run() 