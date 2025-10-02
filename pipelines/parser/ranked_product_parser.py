from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from data_models.ProductRankingResponse import ProductRankingResponse
from langchain_core.output_parsers import PydanticOutputParser

def get_product_ranking_parser() ->  PydanticOutputParser:
    from langchain_core.output_parsers import PydanticOutputParser
    ranking_parser = PydanticOutputParser(pydantic_object=ProductRankingResponse)
    return ranking_parser
