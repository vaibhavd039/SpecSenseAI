from pydantic import BaseModel, Field
from typing import List

class RankedProduct(BaseModel):
    name: str
    hard_matches: List[str] 
    score: float = Field(..., ge=0, le=100, description="Score between 0 and 100")
    soft_matches: List[str] = Field(default_factory=list)
    trade_off: str
    unmet_needs: List[str] = Field(default_factory=list)
    explanation: str
    
