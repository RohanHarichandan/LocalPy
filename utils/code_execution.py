import tokenize
import io
import subprocess
import traceback
import sys

def translate_code(code, translation_map):
    result = []
    tokens = tokenize.generate_tokens(io.StringIO(code).readline)
    for toknum, tokval, _, _, _ in tokens:
        if tokval in translation_map:
            result.append(translation_map[tokval])
        else:
            result.append(tokval)
    return ''.join(result)

# def execute_code(code):
#     try:
#         exec(code)
#     except Exception as e:
#         print(f"Error executing code: {e}")
#         print(traceback.format_exc())
#     finally:
#         # Flush stdout to ensure all output is displayed immediately
#         sys.stdout.flush()

# def execute_code(code):
#     try:
#         output = subprocess.check_output(['python3', '-c', code], stderr=subprocess.STDOUT)
#         return output.decode('utf-8') if output else "No output produced."
#     except subprocess.CalledProcessError as e:
#         # Capture and decode error message from the exception
#         return e.output.decode('utf-8') if e.output else "An error occurred but no output was captured."

# def execute_code(code):
#     # Execute the code using a Python interpreter
#     try:
#         result = eval(code)
#         return str(result)
#     except Exception as e:
#         return str(e)

def execute_code(code):
    # # Create a string buffer to capture output
    # buffer = io.StringIO()
    # # Redirect stdout to the buffer
    # sys.stdout = buffer
    # try:
    #     # Execute the code
    #     exec(code)
    # except Exception as e:
    #     return str(e)
    # finally:
    #     # Restore stdout
    #     sys.stdout = sys.__stdout__
    
    # # Get the output from the buffer
    # return buffer.getvalue()
    
     # Create a string buffer to capture output
     
    # updated code 
    
    buffer = io.StringIO()
    # Redirect stdout to the buffer
    sys.stdout = buffer
    try:
        # Use exec to execute the code
        exec(code)
    except SyntaxError as e:
        return f"Syntax Error: {e.msg} (line {e.lineno})"
    except Exception as e:
        return str(e)
    finally:
        # Restore stdout
        sys.stdout = sys.__stdout__
    
    # Get the output from the buffer
    return buffer.getvalue()