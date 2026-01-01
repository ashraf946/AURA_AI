def get_context_reply(user_message: str, memory: dict) -> str | None:
    """
    Uses short-term memory to maintain simple conversational context.
    """

    last_user_message = memory.get("last_user_message")

    if not last_user_message:
        return None

    msg = user_message.lower()

    # Simple follow-up handling
    if msg in ["yes", "yeah", "yep", "okay", "ok"]:
        return "Got it 👍 Tell me more."

    if msg in ["no", "not really", "nope"]:
        return "Alright 🙂 What would you like to talk about?"

    return None
