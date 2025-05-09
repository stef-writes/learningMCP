from dotenv import load_dotenv
import os
from mcp_instance import mcp
from tools import *
from goals_by_minute_range import *
# from resources import *  # Uncomment if you add resources.py
from prompts import *    # Import prompts

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    mcp.run() 