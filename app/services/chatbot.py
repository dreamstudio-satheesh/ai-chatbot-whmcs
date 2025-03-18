import openai
import os

openai.api_key = os.getenv("OPENROUTER_API_KEY")

def chat_with_ai(user_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
