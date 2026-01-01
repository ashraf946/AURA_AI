def generate_reply(user_message: str, user_name: str = "Ashraf") -> str:
    msg = user_message.lower()

    # Simple rules (safe start)
    if any(word in msg for word in ["hi", "hello", "hey"]):
        return f"Hey {user_name} 👋 How can I help you today?"

    if any(word in msg for word in ["love", "like you"]):
        return f"Aww ❤️ I appreciate that, {user_name}!"

    if any(word in msg for word in ["sad", "down", "upset"]):
        return f"I’m here for you, {user_name}. Want to talk about it?"

    if "who is" in msg or "what is" in msg:
        return "That’s a good question 🤔 I’ll soon answer these intelligently!"

    return "Tell me more 🙂"
