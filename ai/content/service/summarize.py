from ai.content.utils import validate_text, generate_content

def _build_prompt(text: str) -> str:
    return (
        "Summarize the following blog post text concisely in 1 to 2 sentences:\n\n"
        f"{text}"
    )


def summarize_post(content: str) -> dict:
    
    validated_content = validate_text(
        text=content,
        field_name="Content",
        min_length=20
    )

    prompt = _build_prompt(validated_content)
    summary = generate_content(prompt)

    return {
        "summary": summary,
        "length": len(summary),
    }