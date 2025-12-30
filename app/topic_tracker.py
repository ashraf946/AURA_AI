def detect_topic(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["job", "career", "interview", "office", "work"]):
        return "career"

    if any(word in text for word in ["study", "exam", "learn", "college", "course"]):
        return "study"

    if any(word in text for word in ["sad", "happy", "feeling", "emotion", "stress"]):
        return "emotion"

    return "general"
