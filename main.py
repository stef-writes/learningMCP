from dotenv import load_dotenv
import os
from mcp_instance import mcp
from tools import *
from openai_tools import *
from prompts import *    # Import prompts

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    mcp.run() 