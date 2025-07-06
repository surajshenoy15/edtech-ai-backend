import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GRANITE_API_KEY = os.getenv("IBM_GRANITE_API_KEY")
GRANITE_URL = os.getenv("IBM_GRANITE_URL")

def validate_with_granite(content: str) -> str:
    headers = {"Authorization": f"Bearer {GRANITE_API_KEY}"}
    payload = {"text": content, "check_type": "edu-safe"}

    response = httpx.post(GRANITE_URL, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception("Granite validation failed")

    result = response.json()
    return result.get("validated_text", content)
