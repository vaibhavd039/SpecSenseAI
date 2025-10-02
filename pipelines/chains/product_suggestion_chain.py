
import os
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from pipelines.llm_models.gemini_model_provider import get_gemini_llm 
from pipelines.parser.ranked_product_parser import get_product_ranking_parser
from prompt_template.product_suggestio_prompt_template import get_ranking_prompt
from langchain_core.runnables import Runnable
from functools import lru_cache

@lru_cache(1)
def get_product_suggestion_chain() -> tuple[Runnable, str]:
    llm = get_gemini_llm()
    parser = get_product_ranking_parser()
    prompt = get_ranking_prompt()
    chain = prompt| llm| parser
    return chain, parser.get_format_instructions()
