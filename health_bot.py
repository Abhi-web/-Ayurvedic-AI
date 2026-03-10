def get_health_response(user_input):
    user_input = user_input.lower()

    if "fever" in user_input:
        return "For fever, take rest, drink fluids, and consider paracetamol. Consult a doctor if it persists."

    elif "headache" in user_input:
        return "For headache, stay hydrated, rest, and avoid screen time."

    elif "cold" in user_input:
        return "For cold, drink warm fluids and take steam."

    else:
        return "Sorry, I recommend consulting a doctor for proper diagnosis."


print("AI Health Chatbot (type 'exit' to stop)")
while True:
    user = input("You: ")
    if user == "exit":
        break
    print("Bot:", get_health_response(user))