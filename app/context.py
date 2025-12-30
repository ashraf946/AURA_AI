from collections import deque

class ContextMemory:
    def __init__(self, size=5):
        self.history = deque(maxlen=size)

    def add(self, user, sentiment, intent):
        self.history.append({
            "user": user,
            "sentiment": sentiment,
            "intent": intent
        })

    def last(self):
        return self.history[-1] if self.history else None
