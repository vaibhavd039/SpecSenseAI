from pydantic import BaseModel, Field
from typing import List
from .RankedProduct import RankedProduct
from .AlternativeProduct import AlternativeProduct

class ProductRankingResponse(BaseModel):
    no_results: bool
    ranked_products: List[RankedProduct] = Field(default_factory=list)
    alternatives: List[AlternativeProduct] = Field(default_factory=list)