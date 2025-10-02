
import os
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from llm_models.gemini_model_provider import get_gemini_llm 
from parser.filter_extraction_parser import get_pydantic_parser_product_filter
from prompt_template.filter_extraction_prompt_template import get_filter_extraction_prompt
from langchain_core.runnables import Runnable
from functools import lru_cache

@lru_cache(1)
def product_filter_chain() -> tuple[Runnable, str]:
    llm = get_gemini_llm()
    parser = get_pydantic_parser_product_filter()
    prompt = get_filter_extraction_prompt()
    chain = prompt| llm| parser
    return chain , parser.get_format_instructions()
