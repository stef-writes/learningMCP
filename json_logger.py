import json
import datetime
import os
from typing import Any, Dict, Optional

LOG_FILE = "mcp_interactions.log.json"

def log_interaction(tool_name: str, inputs: Dict[str, Any], output: Any, error: Optional[str] = None):
    """
    Logs a tool interaction to a JSON file.
    Each line in the file will be a separate JSON object.
    """
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "tool_name": tool_name,
        "inputs": inputs,
        "output": output,
        "error": error
    }
    
    try:
        # Ensure inputs and output are JSON serializable
        # For complex objects, you might need custom serializers or to_dict() methods
        serializable_inputs = {k: str(v) for k, v in inputs.items()}
        serializable_output = str(output) if not isinstance(output, (dict, list, str, int, float, bool, type(None))) else output

        log_entry["inputs"] = serializable_inputs
        log_entry["output"] = serializable_output

        with open(LOG_FILE, "a") as f:
            json.dump(log_entry, f)
            f.write("\\n")  # Add a newline for each JSON entry
    except Exception as e:
        print(f"Error writing to log file: {e}")
        # Fallback logging to console if file logging fails
        print(f"Fallback log: {log_entry}")

# Example usage (can be removed or commented out)
# if __name__ == "__main__":
#     log_interaction("example_tool", {"param1": "value1", "param2": 123}, {"result": "success"})
#     log_interaction("error_tool", {"param": "test"}, None, "Something went wrong") 