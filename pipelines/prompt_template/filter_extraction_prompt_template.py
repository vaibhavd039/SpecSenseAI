
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))

from langchain_core.prompts import ChatPromptTemplate
from pipelines.utils.filter_extraction_few_shot_loader_util import _load_filter_extraction_few_shot_prompt
from parser.filter_extraction_parser import get_pydantic_parser_product_filter

def get_filter_extraction_prompt():
    FEW_SHOTS =  _load_filter_extraction_few_shot_prompt()
    messages = [
        ("system", "You are an expert at extracting product requirements from user queries into structured filters."),
        ("system", "{format_instructions}"),
    ]

    for user_text, assistant_json in _load_filter_extraction_few_shot_prompt():
        messages.append(("human", user_text))
        messages.append(("ai", assistant_json))

    messages.append(("human", 'Extract hard and soft filters for this query: \"{message}\"'))
    return ChatPromptTemplate.from_messages(messages)
