from pydantic import BaseModel, Field
from typing import List

class AlternativeProduct(BaseModel):
    name: str
    violated_soft_filters: List[str] = Field(default_factory=list)
    hard_matches: List[str]
    soft_matches: List[str] = Field(default_factory=list)
    trade_off: str
    unmet_needs: List[str] = Field(default_factory=list)
    explanation: str