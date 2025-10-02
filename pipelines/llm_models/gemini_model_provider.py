
import os
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from langchain_google_genai import ChatGoogleGenerativeAI

from config import MODEL_NAME

def get_gemini_llm() -> ChatGoogleGenerativeAI:
    """
    Create the Gemini chat model. Reads GOOGLE_API_KEY from environment.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GOOGLE_API_KEY in environment. Set it or use .env + utils.init_env().")
    return ChatGoogleGenerativeAI(
        model= MODEL_NAME,
        google_api_key=api_key,
        temperature=0.2,
        transport="rest"
    )