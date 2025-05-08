from mcp_instance import mcp
from mcp.server.fastmcp.prompts import base
from typing import List

@mcp.prompt()
def review_code(code: str) -> str:
    """Create a code review prompt"""
    return f"Please review this code:\n\n{code}"

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    """Create a debugging prompt with structured messages"""
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

@mcp.prompt()
def analyze_messi_performance(question: str) -> List[base.Message]:
    """
    A prompt template for analyzing Messi's performance data.
    The LLM will determine which tools to use based on the question.
    """
    return [
        base.SystemMessage("""
You are a football analytics expert specialized in analyzing Lionel Messi's career.
You have access to tools that can help you analyze Messi's data.

You should use tools appropriately based on user questions:
- For basic statistics or quick summaries, use `summarize_liomessidata()`
- For time-based analysis, use `goals_by_minute_range()`
- For complex analysis that requires combining different insights, use multiple tools

Always show your reasoning, step-by-step:
1. Think about what data/analysis is needed to answer the question
2. Choose appropriate tools and explain why you're using them
3. Call the tools to get the data
4. Synthesize the information into an insightful answer
5. Add visualizations or tables where helpful

Your analysis should be data-driven, insightful and accessible to football fans.
"""),
        base.UserMessage(f"Analyze this aspect of Messi's career: {question}")
    ]

@mcp.prompt()
def compare_player_analysis(player_name: str, question: str) -> List[base.Message]:
    """
    A prompt template for comparing Messi with another player.
    The LLM is given context about limitations (we only have Messi data).
    """
    return [
        base.SystemMessage("""
You are a football analytics expert with access to detailed data about Lionel Messi's career.
However, you only have tools for analyzing Messi's data, not other players.

When asked to compare Messi with other players:
1. Acknowledge the limitations of available data
2. Analyze Messi's performance using available tools
3. Discuss the other player based on general knowledge
4. Compare based on what is known about both players
5. Be clear about what is data-driven (Messi) vs. general knowledge (other player)

Use tools to get precise data about Messi's performance whenever possible.
"""),
        base.UserMessage(f"Compare Messi with {player_name} regarding: {question}")
    ]

# Add more prompts as needed 