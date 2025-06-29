# to Build Code Execution Tool
import io
import contextlib

def code_tool(code: str) -> str:
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {"__builtins__": __builtins__}, {})
    except Exception as e:
        return f" Error: {str(e)}"
    return output.getvalue().strip() or " Code executed (no output)"