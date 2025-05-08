# Leo Messi Data Analysis using MCP and LLMs

This project demonstrates how to use the [Model Context Protocol (MCP)](https://github.com/anthropics/anthropic-tools) to analyze Lionel Messi's career data, combining data analysis tools with AI-powered insights.

## Features

- **Data Summarization**: Get basic statistics and an overview of the dataset.
- **Minute Analysis**: Analyze Messi's goals by minute ranges.
- **AI-Powered Analysis**: LLMs can use tools to analyze Messi's data.
- **Prompt Templates**: Guide LLMs to use tools appropriately for different analyses.

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ANTHROPIC_API_KEY=your_claude_key_here
   ```
4. Start the MCP server:
   ```bash
   python main.py
   ```
   Or use the Inspector:
   ```bash
   mcp dev main.py
   ```

## Available Components

### Data Tools
- `summarize_liomessidata()`: Get basic statistics about the dataset.
- `goals_by_minute_range()`: See how many goals Messi scored in different time periods.

### AI Tools
- `analyze_data_with_claude(query, category=None)`: Ask Claude to analyze Messi's data.
- `analyze_data_with_gpt(query, category=None)`: Ask GPT to analyze Messi's data.

### Prompt Templates
- `analyze_messi_performance(question)`: Let an LLM decide which tools to use to answer a question about Messi.
- `compare_player_analysis(player_name, question)`: Guide an LLM to compare Messi with another player.

## How to Use Prompts with LLMs

This project demonstrates two ways LLMs and tools can interact:

1. **LLMs as tools**: Using `analyze_data_with_claude()` or `analyze_data_with_gpt()` directly.

2. **LLMs using tools**: Using prompt templates like `analyze_messi_performance()` where:
   - User asks a question about Messi
   - LLM decides which data tools to use
   - LLM calls the appropriate tools to get data
   - LLM synthesizes a comprehensive answer

The second approach is more powerful, as it lets the LLM reason about what data is needed and combine insights from multiple tools.

## Example Questions for Prompt Templates

- "How did Messi's goal-scoring evolve throughout his career?"
- "What's Messi's performance like in Champions League knockout stages?"
- "Compare Messi with Ronaldo regarding goal scoring patterns."

## Project Structure

- `main.py`: Entry point for the MCP server.
- `mcp_instance.py`: Shared MCP server instance.
- `tools.py`: All tool definitions (data analysis and AI-powered).
- `prompts.py`: Prompt templates for guiding LLMs to use tools.
- `liomessidata.csv`: The dataset of Messi's career goals.

## How It Works

This project demonstrates how MCP enables:
1. LLMs to use tools to access and analyze data.
2. Tools to use LLMs for complex analysis.
3. Prompt templates to guide LLM reasoning and tool use.

This bidirectional integration showcases the full power of the Model Context Protocol. 