def text_analyzer(text: str) -> dict:
    """
    Analyze input text and return factual properties.

    This is a pure, deterministic tool:
    - It does NOT decide success/failure
    - It does NOT compute confidence
    - It does NOT touch agent state
    """

    # 1. Validate input type (hard failure)
    if not isinstance(text, str):
        raise ValueError("Input text must be a string")

    # 2. Normalize input
    normalized_text = text.strip()

    # 3. Extract factual properties
    if normalized_text == "":
        word_count = 0
    else:
        word_count = len(normalized_text.split())

    # 4. Return structured facts
    return {
        "word_count": word_count,
        "is_empty": word_count == 0,
    }
