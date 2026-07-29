from ai.content.utils import validate_text, generate_content


def _build_generate_prompt(title: str, tone: str = None) -> str:
    """Private helper to format the AI prompt for generation."""
    prompt = f"Write a short blog post about: {title}."

    if tone:
        prompt += f" Write it in a {tone} tone."

    prompt += " Keep the total output under 500 characters."

    return prompt


def generate_post(title: str, tone: str = None) -> dict:
    cleaned_title = validate_text(
        text=title,
        field_name="Title",
        min_length=5,
    )

    prompt = _build_generate_prompt(cleaned_title, tone)
    content = generate_content(prompt)

    if len(content) > 500:
        content = content[:500]

    return {
        "title": cleaned_title,
        "content": content,
        "length": len(content),
    }