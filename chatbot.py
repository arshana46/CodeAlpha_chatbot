import random
import datetime

def chatbot():
    print("🤖 Chatbot: Hey there! I'm your friendly Python bot 💬")
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐞",
        "Why was the computer cold? It left its Windows open! 💻",
        "I told my computer I needed a break — and it said 'No problem, I’ll go to sleep!' 😴"
    ]

    facts = [
        "Did you know? Python was named after 'Monty Python', not the snake!",
        "The first computer mouse was made of wood 🖱️",
        "Email was invented before the World Wide Web existed 🌐"
    ]

    quotes = [
        "Believe you can, and you're halfway there. 💪",
        "Keep learning — every expert was once a beginner. 🌱",
        "Stay positive, work hard, and make it happen! ✨"
    ]

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hi there! How’s your day going? 😊")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I’m feeling smart and chatty today! How about you?")

        elif "good" in user_input or "fine" in user_input:
            print("🤖 Chatbot: Awesome! Keep up the good vibes ✨")

        elif "your name" in user_input:
            print("🤖 Chatbot: I'm PyBot — your Python-powered chat friend 🐍")

        elif "what can you do" in user_input or "help" in user_input:
            print("🤖 Chatbot: I can tell jokes, fun facts, motivational quotes, or just chat with you!")

        elif "joke" in user_input:
            print("😂 " + random.choice(jokes))

        elif "fact" in user_input:
            print("🤓 " + random.choice(facts))

        elif "quote" in user_input or "motivate" in user_input:
            print("💡 " + random.choice(quotes))

        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(f"⏰ The current time is {now}")

        elif "date" in user_input or "day" in user_input:
            today = datetime.date.today().strftime("%A, %B %d, %Y")
            print(f"📅 Today is {today}")

        elif "thank" in user_input:
            print("🤖 Chatbot: You’re most welcome! Glad to chat anytime 😊")

        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a wonderful day 🌸")
            break

        else:
            print("🤖 Chatbot: Hmm, I didn’t quite get that. Try saying 'joke', 'fact', 'quote', or 'time'.")

# Run chatbot
chatbot()
