import os
from openai import OpenAI # type: ignore

def ask_chatgpt(prompt: str) -> str:
    """
    Calls ChatGPT ONLY when local AI is not confident.
    Uses the latest OpenAI Python SDK syntax.
    """

    # API key is automatically read from environment variable
    # OPENAI_API_KEY
    try:
        client = OpenAI()

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            max_output_tokens=200,
            temperature=0.7
        )

        return response.output_text.strip()

    except Exception as e:
        print("OpenAI error:", e)
        return "I couldn’t reach my cloud brain right now. Let’s continue together."
