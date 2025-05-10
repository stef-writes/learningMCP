# MCP Test Project

A minimal project to test and verify MCP functionality.

## Features

- **Basic Tools**: Simple tools to verify MCP is working correctly
- **Test Prompt**: A basic prompt template for testing MCP functionality

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the MCP server:
   ```bash
   python main.py
   ```
   Or use the Inspector:
   ```bash
   mcp dev main.py
   ```

## Available Components

### Tools
- `hello_world()`: A simple tool that returns a greeting to verify MCP is working
- `debug_info()`: Displays environment information and configuration status

### Prompt Templates
- `test_prompt(message)`: A basic prompt template for testing MCP functionality

## Project Structure

- `main.py`: Entry point for the MCP server
- `mcp_instance.py`: Shared MCP server instance
- `tools.py`: Basic tool definitions
- `prompts.py`: Simple prompt template for testing

## Troubleshooting

If you encounter any issues:
1. Check the debug_info() tool output for environment details
2. Verify your Python environment is set up correctly
3. Ensure all dependencies are installed 