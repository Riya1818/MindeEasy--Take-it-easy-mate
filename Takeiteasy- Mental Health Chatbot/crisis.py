from typing import List

# Keywords used to detect potential crisis situations in user input.
CRISIS_KEYWORDS: List[str] = [
    "suicidal", "suicide", "kill myself", "want to die", "hopeless", "worthless",
    "can't go on", "give up", "ending it all", "no reason to live"
]

# Message containing resources and support helplines to be displayed in a crisis.
SAFETY_MESSAGE = (
    "It sounds like you're going through a really tough time."
    "\n"
    "You're not alone, and there are people who want to help you."
    "\n\n"
    "Please consider reaching out to a mental health professional or contacting a helpline:\n\n"
    "***India:** 9152987821 (iCall), 1800-599-0019 (Vandrevala Foundation)\n"
    "***USA:** 988 (Suicide & Crisis Lifeline)\n"
    "***UK:** 116 123 (Samaritans)\n\n"
    "You matter. 💙"
)

def contains_crisis_keywords(text: str) -> bool:
    """
    Checks if the input text contains any of the defined crisis keywords.
    The check is case-insensitive.
    """
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)