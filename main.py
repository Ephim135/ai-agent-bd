import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Error: at least one argument is required but u provided 0")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Error: usage 'prompt' '--verbose'(optional)")
    sys.exit(1)

user_prompt = sys.argv[1]
verbose = False
if len(sys.argv) == 3:
    if sys.argv[2] == "--verbose":
        verbose = True
    else:
        print("Error: wrong optional argument")
        sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)

print(response.text)
if verbose:
    print("User prompt: ", user_prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count, "\nResponse tokens:", response.usage_metadata.candidates_token_count)

