INTENT_KEYWORDS = {
    "greeting": ["hi", "hello", "hey"],
    "affection": ["love", "miss", "like you"],
    "gratitude": ["thank", "thanks"],
    "help": ["help", "support", "guide"],
    "emotion_negative": ["sad", "down", "upset", "depressed"],
    "emotion_positive": ["happy", "excited", "great"],
    "goodbye": ["bye", "good night", "see you"]
}

def detect_intent(text: str) -> str:
    text = text.lower()

    for intent, words in INTENT_KEYWORDS.items():
        for w in words:
            if w in text:
                return intent

    return "general"
