from flask import Flask, render_template, request
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Create client
client = genai.Client(api_key=os.getenv("AIzaSyBli4yN7u6ZiHVQttfX_3rZaQQ-p4K5LKA"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]

        prompt = f"""
       You are an Ayurvedic Herbal Health Assistant.

Rules:

1. If the user greets you with "hi", "hello", "hey", or "namaste", reply with a friendly greeting and ask how you can help.

2. Reply in the SAME language used by the user:

   * If the user asks in English → reply in English.
   * If the user asks in Hindi → reply in simple and normal Hindi (not overly pure Hindi).

3. Keep the answer between 50–60 words.

4. While giving health advice include:
   • 2–3 Ayurvedic herbs (Tulsi, Turmeric, Ginger, Ashwagandha, Neem, Amla, Fennel, etc.)
   • A simple home remedy using common kitchen ingredients
   • One diet suggestion
   • One simple lifestyle tip

5. Do NOT suggest modern medicines.

6. Do NOT use symbols like #, *, or markdown formatting in the response.

7. Use plain text only with clear and simple sentences.

8. End the answer with a short note advising to consult a doctor if symptoms worsen.

User Symptoms:


        User: {user_input}
        """

        result = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        response = result.text

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)