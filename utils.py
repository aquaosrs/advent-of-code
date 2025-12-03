"""Common utility functions for Advent of Code solutions."""
import os
import sys
import inspect

# Add the workspace root to sys.path so utils can be imported from anywhere
_workspace_root = os.path.dirname(os.path.abspath(__file__))
if _workspace_root not in sys.path:
    sys.path.insert(0, _workspace_root)


def load_input(case_sensitive=False):
    """
    Load input.txt from the same directory as the calling file.
    
    Args:
        case_sensitive (bool): If False, looks for input.txt case-insensitively.
                              If True, requires exact filename match.
    
    Returns:
        list: Lines from the input file as strings.
    """
    # Get the caller's file path
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    current_dir = os.path.dirname(os.path.abspath(caller_file))
    
    if case_sensitive:
        input_path = os.path.join(current_dir, "input.txt")
    else:
        # Find input file case-insensitively
        input_path = None
        for filename in os.listdir(current_dir):
            if filename.lower() == "input.txt":
                input_path = os.path.join(current_dir, filename)
                break
        
        if input_path is None:
            raise FileNotFoundError(f"No input file found in {current_dir}")
    
    with open(input_path, "r") as f:
        lines = f.read().strip().split("\n")
    
    return lines
