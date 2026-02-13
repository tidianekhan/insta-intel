import random


def generate_summary(caption: str) -> dict:
    """
    Mock summary generator.
    Replace with real OpenAI call later.
    """

    return {
        "summary": f"This post discusses {caption[:60]}...",
        "pillar": random.choice(["Education", "Product", "Engagement", "Brand"]),
        "themes": ["Cybersecurity", "Awareness"],
        "confidence_score": round(random.uniform(0.7, 0.95), 2)
    }
