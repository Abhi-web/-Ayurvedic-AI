from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Load API key from environment
client = genai.Client(api_key=os.getenv("AIzaSyBli4yN7u6ZiHVQttfX_3rZaQQ-p4K5LKA"))

def get_ai_response(user_input):
    prompt = f"""
    You are a professional medical assistant.
    Give safe and general health advice.
    Always suggest consulting a doctor.

    User: {user_input}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


print("AI Health Assistant (type 'exit' to stop)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break

    print("Bot:", get_ai_response(user))