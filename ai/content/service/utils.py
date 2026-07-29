from ai.content.content_client import ContentClient


def validate_text(text: str, field_name: str, min_length: int) -> str:
    """Shared validation for text inputs."""
    if not text or not text.strip():
        raise ValueError(f"{field_name} cannot be empty or whitespace.")

    cleaned = text.strip()

    if len(cleaned) < min_length:
        raise ValueError(
            f"{field_name} must be at least {min_length} characters long."
        )

    return cleaned


def generate_content(prompt: str) -> str:
    """Shared AI generation pipeline."""
    client = ContentClient()
    result = client.generate(prompt).strip()

    if not result:
        raise ValueError("Model output was empty or invalid.")

    return result