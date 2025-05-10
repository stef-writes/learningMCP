from mcp_instance import mcp
import openai
import os
from dotenv import load_dotenv
from json_logger import log_interaction
import json
import datetime # Added for print timestamp

# Load environment variables
load_dotenv()

# Initialize OpenAI client with a longer timeout for potentially complex outline generation
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=60.0,  # Increased timeout to 60 seconds
    max_retries=2
)

@mcp.tool()
def say_hello() -> str:
    """Test OpenAI connection with a simple hello."""
    tool_name = "say_hello"
    inputs = {}
    output = None
    error = None
    llm_call_details = None
    try:
        response_obj = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=10
        )
        output = response_obj.choices[0].message.content
        llm_call_details = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": "Say hello"}],
            "response_id": response_obj.id,
            "finish_reason": response_obj.choices[0].finish_reason,
            "usage": dict(response_obj.usage) if hasattr(response_obj, 'usage') and response_obj.usage is not None else None
        }
        return output
    except Exception as e:
        error = str(e)
        return f"Error in {tool_name}: {error}"
    finally:
        current_inputs = inputs.copy()
        if llm_call_details:
            current_inputs["_llm_call_details"] = llm_call_details
        log_interaction(tool_name, current_inputs, output, error)

@mcp.tool()
def generate_analytical_outline(question: str) -> str:
    """
    Takes a question and returns a structured analytical outline 
    (chain of thought) that an LLM could use to break down the problem.
    Does not provide the solution, only the process outline.
    """
    tool_name = "generate_analytical_outline"
    inputs = {"question": question}
    output = None
    error = None
    llm_call_details = None
    
    print(f"[{datetime.datetime.now()}] DEBUG: Entering {tool_name} with question: {question[:50]}...") # DEBUG

    system_prompt = ("""
    You are an expert in problem decomposition and analytical thinking. 
    Given a user's question, your task is to generate a structured outline 
    that an LLM could follow to perform a granular analysis of the problem. 
    Do NOT provide an answer or solution to the question itself. 
    Focus ONLY on outlining the chain of thought or analytical process.

    The outline should include:
    1.  Clarification of the core problem/question.
    2.  Identification of key sub-questions or components.
    3.  A logical sequence of analytical steps.
    4.  Types of information or data that would be relevant (even if hypothetical).
    5.  Potential assumptions or ambiguities to address.
    6.  Possible reasoning paths or frameworks to consider.

    Present the outline in a clear, structured format (e.g., markdown bullet points or numbered lists).
    Keep the outline concise but comprehensive, aiming for around 300-400 tokens.
    """)
    
    user_message = f"Generate an analytical outline for the following question: {question}"
    
    messages_to_llm = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    
    try:
        print(f"[{datetime.datetime.now()}] DEBUG: Calling OpenAI API for {tool_name}...") # DEBUG
        response_obj = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_to_llm,
            temperature=0.4, 
            max_tokens=500   
        )
        print(f"[{datetime.datetime.now()}] DEBUG: OpenAI API call completed for {tool_name}.") # DEBUG
        output = response_obj.choices[0].message.content
        llm_call_details = {
            "model": "gpt-4o-mini",
            "messages_sent": messages_to_llm,
            "response_id": response_obj.id,
            "finish_reason": response_obj.choices[0].finish_reason,
            "usage": dict(response_obj.usage) if hasattr(response_obj, 'usage') and response_obj.usage is not None else None,
        }
        print(f"[{datetime.datetime.now()}] DEBUG: Exiting {tool_name} successfully.") # DEBUG
        return output
    except openai.Timeout as e:
        error = f"OpenAI API request timed out: {e}"
        print(f"[{datetime.datetime.now()}] DEBUG: OpenAI Timeout in {tool_name}: {error}") # DEBUG
        llm_call_details = {"model": "gpt-4o-mini", "messages_sent": messages_to_llm, "error": str(e)}
        return f"Error in {tool_name}: {error}"
    except openai.APIError as e:
        error = f"OpenAI API returned an API Error: {e}"
        print(f"[{datetime.datetime.now()}] DEBUG: OpenAI APIError in {tool_name}: {error}") # DEBUG
        llm_call_details = {"model": "gpt-4o-mini", "messages_sent": messages_to_llm, "error": str(e)}
        return f"Error in {tool_name}: {error}"
    except Exception as e:
        error = str(e)
        print(f"[{datetime.datetime.now()}] DEBUG: Unexpected error in {tool_name}: {error}") # DEBUG
        llm_call_details = {"model": "gpt-4o-mini", "messages_sent": messages_to_llm, "error": str(e)}
        return f"Error in {tool_name}: An unexpected error occurred: {error}"
    finally:
        current_inputs = inputs.copy()
        if llm_call_details:
            current_inputs["_llm_call_details"] = llm_call_details
        log_interaction(tool_name, current_inputs, output, error) 