import requests
import os
from dotenv import load_dotenv

load_dotenv()

def ask_ai(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if response.status_code != 200 or "choices" not in data:
        print("Groq API ERROR:", data)
        return "⚠️ AI service temporarily unavailable. Please try again."

    return data["choices"][0]["message"]["content"]
