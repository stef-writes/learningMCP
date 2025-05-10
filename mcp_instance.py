from mcp.server.fastmcp import FastMCP

# Configure MCP with specific settings
mcp = FastMCP(
    "Data Analysis Workspace",
    request_timeout=60,  # Longer timeout
    sse_retry_timeout=1000,  # Longer SSE retry timeout
    keep_alive=True  # Keep connection alive
) 