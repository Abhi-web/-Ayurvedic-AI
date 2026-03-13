 ![Ayurvedic AI Demo](https://github.com/Abhi-web/-Ayurvedic-AI/blob/91fc46de72bd5af98f2e8df830e8724a2195134c/Screenshot%202026-03-13%20204233.png)
                                                         
                                                         🌿 Ayurvedic AI Health Assistant
An AI-powered web application that provides **Ayurvedic health guidance** based on user symptoms.
The assistant suggests **natural herbs, home remedies, diet tips, and lifestyle recommendations** using AI.

This project combines **Flask (Python backend)** with **Google Gemini AI** to generate intelligent health responses.

---

🚀 Features

* 🌿 **AI Ayurvedic Guidance** – Suggests natural herbs and remedies
* 🧠 **AI-Powered Responses** – Uses Google Gemini AI model
* 🎤 **Voice Assistant Support** – Speak symptoms using microphone
* 💬 **Interactive Chat Interface** – Simple and clean user interface
* ⚡ **Instant AI Responses** – Real-time symptom analysis
* 📱 **Responsive Design** – Works on desktop and mobile
* 🧘 **Holistic Health Suggestions** – Diet and lifestyle recommendations

---
🛠️ Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python
* Flask

**AI Model**

* Google Gemini API

**Other Tools**

* Python Dotenv
* Speech Recognition API
* Web Speech API

---

📂 Project Structure

```
AYURVEDIC-AI-HEALTH-ASSISTANT/
│
├── templates/
│   └── index.html
│
├── venv/
│
├── .env
├── ai_health_bot.py
├── app.py
├── health_bot.py
├── README.md
└── requirements.txt
```

---

⚙️ Installation

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/ayurvedic-ai-assistant.git
cd ayurvedic-ai-assistant
```

---
2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```
Mac / Linux

```
source venv/bin/activate
```

---
3️⃣ Install dependencies

```
pip install flask google-genai python-dotenv
```

---
4️⃣ Add API key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

---
5️⃣ Run the application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```
🎤 Voice Assistant

Users can interact with the AI using voice:

1. Click the **microphone button**
2. Speak your symptoms
3. AI converts speech to text
4. Response is generated and spoken back

---

⚠️ Disclaimer

This AI assistant provides **general wellness guidance based on Ayurvedic principles**.
It is **not a substitute for professional medical advice**.
Always consult a qualified healthcare professional for serious health conditions.

---
⭐ Support

If you like this project:

* Star the repository ⭐
* Share feedback
* Contribute improvements

---
📌 Future Improvements

* AI chat memory
* Ayurvedic dosha analysis (Vata / Pitta / Kapha)
* Advanced voice conversation
* Health report generation
* Deployment on cloud
