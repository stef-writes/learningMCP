from mcp_instance import mcp
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@mcp.tool()
def say_hello() -> str:
    """Test OpenAI connection with a simple hello."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=10
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}" 