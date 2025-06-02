import os
import openai
from dotenv import load_dotenv

# Load the API key from .env (optional, safer)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # or "gpt-3.5-turbo" if you're on the free tier
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"API Error: {e}"

if __name__ == "__main__":
    print("AI ChatBot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'break']:
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("AI:", response)
