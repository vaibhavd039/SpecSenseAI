from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from pipelines.data_models.ProductFilters import ProductFilters
from langchain_core.output_parsers import PydanticOutputParser

def get_pydantic_parser_product_filter() -> PydanticOutputParser:
    from langchain_core.output_parsers import PydanticOutputParser
    parser = PydanticOutputParser(pydantic_object=ProductFilters)
    return parser
