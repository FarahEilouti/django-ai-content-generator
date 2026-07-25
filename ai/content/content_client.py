import os
from openai import OpenAI
from decouple import config
class ContentClient:
    """Boundary layer for interacting with OpenAI API."""

    def __init__(self):
        # Fetch key from environment / .env
        api_key = config("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        # Using a fast, cheap model suitable for text summarization
        self.model = "gpt-4o-mini"

    def generate(self, prompt: str) -> str:
        """Sends prompt to OpenAI and returns raw string content."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content or ""