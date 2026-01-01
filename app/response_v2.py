from app.intent_v2 import detect_intent
from app.personality import get_personality_reply
from app.context import get_context_reply
from app.llm_client import ask_chatgpt


# Keywords that indicate real-world / factual questions
KNOWLEDGE_KEYWORDS = [
    "who is", "what is", "when", "where", "why", "how",
    "ceo", "founder", "capital", "president",
    "explain", "define", "meaning of"
]


def is_knowledge_question(message: str) -> bool:
    msg = message.lower()
    return any(keyword in msg for keyword in KNOWLEDGE_KEYWORDS)


def generate_response_v2(user_message: str, user_name: str, memory: dict) -> str:
    """
    Main brain of AURA AI v2
    """

    # 1️⃣ Force ChatGPT for factual / knowledge questions
    if is_knowledge_question(user_message):
        return ask_chatgpt(user_message)

    # 2️⃣ Context-aware reply (short-term memory)
    context_reply = get_context_reply(user_message, memory)
    if context_reply:
        return context_reply

    # 3️⃣ Intent + personality-based reply
    intent = detect_intent(user_message)
    personality_reply = get_personality_reply(intent, user_name)
    if personality_reply:
        return personality_reply

    # 4️⃣ Final fallback → ChatGPT
    return ask_chatgpt(user_message)
