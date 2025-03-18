import openai
import os

openai.api_key = os.getenv("OPENROUTER_API_KEY")

def chat_with_ai(user_input: str):
    response = openai.ChatCompletion.create(
        model="google/gemma-3-27b-it:free",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
