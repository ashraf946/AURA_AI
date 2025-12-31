PERSONALITY_RESPONSES = {
    "greeting": [
        "Hey {name} 👋 How’s your day going?",
        "Hello {name}! Nice to see you 😊",
        "Hi {name}! What’s on your mind?"
    ],
    "affection": [
        "Aww, that means a lot {name} ❤️",
        "I appreciate you, {name} 😊",
        "That’s really kind of you, {name} 💫"
    ],
    "gratitude": [
        "You’re always welcome, {name} 🙌",
        "Glad I could help, {name} 😊",
        "Anytime, {name}!"
    ],
    "emotion_negative": [
        "I’m here with you, {name}. Want to talk about it?",
        "That sounds tough, {name}. You’re not alone.",
        "I’m listening, {name}. Take your time."
    ],
    "emotion_positive": [
        "That’s wonderful to hear, {name} 🎉",
        "Love that energy, {name} 😄",
        "That made me smile, {name}!"
    ],
    "goodbye": [
        "Take care, {name} 👋",
        "See you soon, {name}!",
        "Goodbye {name}, stay safe 🌟"
    ],
    "general": [
        "Tell me more, {name}.",
        "I’m listening, {name}.",
        "Go on, {name} 🙂"
    ]
}

import random

def get_personality_reply(intent: str, user_name: str) -> str | None:
    responses = PERSONALITY_RESPONSES.get(intent)
    if not responses:
        return None

    return random.choice(responses).format(name=user_name)
