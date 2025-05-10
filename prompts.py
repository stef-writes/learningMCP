from mcp_instance import mcp
from mcp.server.fastmcp.prompts import base
from typing import List

@mcp.prompt()
def test_prompt(message: str) -> List[base.Message]:
    """
    A simple test prompt to verify MCP is working correctly.
    """
    system_instructions = """
    You are a helpful assistant that can use tools to help users.
    You have access to:
    1. hello_world() - A basic test tool
    2. say_hello() - A test tool that uses OpenAI

    Try both tools to verify everything is working.
    """
    return [
        base.Message(role="user", content=f"{system_instructions}\n\nUser question: Please test the tools: {message}")
    ]

@mcp.prompt()
def get_problem_breakdown_outline(user_question: str) -> List[base.Message]:
    """
    Prompt to get a structured analytical outline for a given question.
    Uses the generate_analytical_outline tool.
    """
    system_instructions = """
    You are an AI assistant that helps users break down complex problems.
    You have a tool called `generate_analytical_outline` that takes a question 
    and returns a structured outline of how an LLM could analyze it.
    Your goal is to use this tool to provide the user with that outline.
    Present the outline clearly.
    """
    return [
        base.Message(role="user", content=f"{system_instructions}\n\nUser task: I need help understanding how to approach this problem: {user_question}")
    ]

@mcp.prompt()
def quick_prompt(message: str) -> List[base.Message]:
    """
    Simple prompt for quick GPT-4 responses.
    """
    system_instructions = """
    You are a helpful assistant with access to GPT-4 through the quick_chat tool.
    Use this tool to give very brief responses to the user's messages.
    Keep everything concise.
    """
    return [
        base.Message(role="user", content=f"{system_instructions}\n\nUser message: {message}")
    ]
