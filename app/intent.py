def detect_intent(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "greeting"

    if any(word in text for word in ["bye", "goodbye", "see you"]):
        return "goodbye"

    if any(word in text for word in ["thank", "thanks"]):
        return "gratitude"

    if any(word in text for word in ["love you", "i love you"]):
        return "affection"

    if any(word in text for word in ["help", "support"]):
        return "help"

    return "unknown"
