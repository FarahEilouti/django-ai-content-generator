from ai.content.content_client import ContentClient

def _build_prompt(text: str) -> str:
    """Private helper to format the AI prompt (kept in exactly one place)."""
    return f"Summarize the following blog post text concisely in 1 to 2 sentences:\n\n{text}"

def summarize_post(text: str) -> dict:
    """
    Service pipeline:
    1. Input validation
    2. AI processing
    3. Post-processing
    4. Response formatting
    """
    # --- Stage 1: Input validation ---
    if not text or not text.strip():
        raise ValueError("Content cannot be empty or whitespace.")

    cleaned_text = text.strip()
    if len(cleaned_text) < 20:
        raise ValueError("Content must be at least 20 characters long.")

    # --- Stage 2: AI processing ---
    prompt = _build_prompt(cleaned_text)
    client = ContentClient()
    raw_summary = client.generate(prompt)

    # --- Stage 3: Post-processing ---
    cleaned_summary = raw_summary.strip()
    if not cleaned_summary:
        raise ValueError("Model output was empty or invalid.")

    # --- Stage 4: Response formatting ---
    return {
        "summary": cleaned_summary,
        "length": len(cleaned_summary)
    }

#-------------assignement addings (25 July 2026) -----------------------

def _build_generate_prompt(title: str, tone: str = None) -> str:
    """Private helper to format the AI prompt for generation."""
    prompt = f"Write a short blog post about: {title}."
    if tone:
        prompt += f" Write it in a {tone} tone."
    
    # Instructing the AI to respect the 500-character limit mentioned in the requirements
    prompt += " Keep the total output under 500 characters."
    return prompt

def generate_post(title: str, tone: str = None) -> dict:
    """
    Service pipeline for generating a blog post:
    1. Validation
    2. AI Processing
    3. Cleaning
    4. Formatting
    """
    # --- Stage 1: Input validation ---
    if not title or not title.strip():
        raise ValueError("Title cannot be empty or whitespace.")

    cleaned_title = title.strip()
    if len(cleaned_title) < 5:
        raise ValueError("Title must be at least 5 characters long.")

    # --- Stage 2: AI processing ---
    prompt = _build_generate_prompt(cleaned_title, tone)
    
    # Reusing the exact same client from the previous task!
    client = ContentClient() 
    raw_content = client.generate(prompt)

    # --- Stage 3: Post-processing ---
    cleaned_content = raw_content.strip()
    if not cleaned_content:
        raise ValueError("Model output was empty or invalid.")
        
    # Strictly enforcing the max 500 characters rule just in case the AI ignores the prompt
    if len(cleaned_content) > 500:
        cleaned_content = cleaned_content[:500]

    # --- Stage 4: Response formatting ---
    return {
        "title": cleaned_title,
        "content": cleaned_content,
        "length": len(cleaned_content)
    }