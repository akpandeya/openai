import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:

    prompt = input("> ")
    if prompt == "q" or prompt == "e":
        print("Exiting...")
        break
    response = openai.Completion.create(
        engine="code-davinci-002", prompt=prompt, max_tokens=15000
    )

    print(response.choices[0].text)
