import random
from app.sentiment import analyze_sentiment
from app.intent_v2 import detect_intents
from app.topic_tracker import detect_topic

def generate_response_v2(text, memory, context):
    sentiment = analyze_sentiment(text)
    intents = detect_intents(text)
    topic = detect_topic(text)

    name = memory.get("user_name", "Ashraf")

    dominant_intent = max(intents, key=intents.get)
    context.add(text, sentiment, dominant_intent)

    # ---------------- CHATGPT-LIKE REPLIES ----------------

    if dominant_intent == "affection":
        return (
            f"Aww 💖 I really appreciate that, {name}. "
            "Positive energy like this makes conversations better. "
            "How are you feeling right now?"
        )

    if dominant_intent == "greeting":
        return (
            f"Hey {name} 👋 It’s nice to see you again. "
            "How’s your day going so far?"
        )

    if sentiment == "negative":
        return (
            "I’m really sorry you’re feeling this way 😔. "
            "Do you want to talk about what’s been bothering you?"
        )

    if sentiment == "positive":
        return (
            "That’s great to hear 😊. "
            "What’s been going well for you?"
        )

    # Neutral / default (ChatGPT-like)
    return (
        "I’m listening 👂. "
        "Tell me a bit more so I can understand you better."
    )
