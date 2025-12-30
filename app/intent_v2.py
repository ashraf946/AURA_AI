INTENT_KEYWORDS = {
    "greeting": ["hi", "hello", "hey"],
    "affection": ["love", "miss", "like you"],
    "gratitude": ["thank", "thanks"],
    "help": ["help", "support", "guide"],
    "emotion_negative": ["sad", "down", "upset", "depressed"],
    "emotion_positive": ["happy", "excited", "great"],
    "goodbye": ["bye", "good night", "see you"]
}

def detect_intents(text: str) -> dict:
    text = text.lower()
    scores = {intent: 0 for intent in INTENT_KEYWORDS}

    for intent, words in INTENT_KEYWORDS.items():
        for w in words:
            if w in text:
                scores[intent] += 1

    return scores
