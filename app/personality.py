import random

PERSONALITY = {
    "warm": [
        "I’m here with you 😊",
        "That means a lot 💙",
        "I really appreciate that"
    ],
    "supportive": [
        "You don’t have to go through this alone",
        "I’ve got your back",
        "It’s okay to feel this way"
    ],
    "cheerful": [
        "That’s awesome 😄",
        "Yay! That sounds great!",
        "Love that energy ✨"
    ]
}

def apply_personality(mood: str) -> str:
    return random.choice(PERSONALITY.get(mood, PERSONALITY["warm"]))
