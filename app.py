import openai 
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

def generate_response(conversation_history):
    completions = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=conversation_history,
        # max_tokens = 12,
        n = 1,
        temperature=0,
    )
    message = completions.choices[0].message.content
    return message
