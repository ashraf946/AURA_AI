import random
from app.intent import detect_intent
from app.sentiment import analyze_sentiment
from data.memory_db import save_user


def generate_response(user_text: str, memory: dict) -> dict:
    intent = detect_intent(user_text)
    sentiment = analyze_sentiment(user_text)

    name = memory.get("user_name")

    # ---------------- NAME & PERSONALIZATION ----------------
    if name is None:
        if "my name is" in user_text.lower():
            name = user_text.split()[-1].capitalize()
            memory["user_name"] = name

            reply = random.choice([
                f"Nice to meet you, {name}! 😊",
                f"Great to know you, {name}! 🌟",
                f"Hello {name}! I’m really glad to meet you 😊"
            ])

            return {
                "reply": reply,
                "intent": "introduction",
                "sentiment": sentiment
            }
        else:
            return {
                "reply": random.choice([
                    "Before we continue, may I know your name? 😊",
                    "I’d love to know your name first 🌟",
                    "Can you tell me your name? 🙂"
                ]),
                "intent": "ask_name",
                "sentiment": sentiment
            }

    # ---------------- CONTEXT AWARENESS ----------------
    if memory.get("last_sentiment") == "negative" and sentiment == "negative":
        reply = random.choice([
            "I can feel you’re still going through something 😔. Want to share more?",
            "It seems the feeling hasn’t eased yet 💙. I’m right here with you.",
            "Take your time 🌱 I’m listening."
        ])
    else:
        reply = None

    # ---------------- INTENT-BASED RESPONSES ----------------
    if intent == "greeting":
        reply = random.choice([
            f"Welcome back, {name} 👋 How are you today?",
            f"Hey {name}! 😊 How’s your day going?",
            f"Hello {name}! What’s on your mind today?"
        ])

    elif intent == "affection":
        reply = random.choice([
            f"Aww ❤️ that really means a lot, {name}!",
            f"That’s so sweet, {name} 🥰",
            f"You just made my day, {name} 💫"
        ])

    elif intent == "gratitude":
        reply = random.choice([
            "You’re always welcome 🌟",
            "Happy to help 😊",
            "Anytime! 🙌"
        ])

    elif intent == "goodbye":
        reply = random.choice([
            f"Goodbye, {name} 👋 Take care!",
            f"See you soon, {name} 🌟",
            f"Bye {name}! Stay positive 😊"
        ])

    # ---------------- SENTIMENT FALLBACK ----------------
    if reply is None:
        if sentiment == "negative":
            reply = random.choice([
                "I’m really sorry you’re feeling this way 😔",
                "That sounds tough 💙 I’m here for you.",
                "It’s okay to feel like this sometimes 🌱"
            ])
        elif sentiment == "positive":
            reply = random.choice([
                "That’s wonderful to hear 😊",
                "I’m glad things are going well for you 🌟",
                "That sounds positive! Tell me more ✨"
            ])
        else:
            reply = random.choice([
                "I’m listening 👂",
                "Go on, I’m here 😊",
                "Tell me more 💭"
            ])

    # ---------------- SAVE CONTEXT & LONG-TERM MEMORY ----------------
    memory["last_sentiment"] = sentiment

    if name:
        save_user(name, sentiment)

    return {
        "reply": reply,
        "intent": intent,
        "sentiment": sentiment
    }
