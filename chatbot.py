import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv

# Load the API key from .env (optional, safer)
load_dotenv()

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(model="gpt-4-turbo", 
        messages=[{"role": "user", "content": prompt}])
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

