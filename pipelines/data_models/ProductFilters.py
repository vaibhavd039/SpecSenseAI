from pydantic import BaseModel, Field
from typing import List, Optional

class ProductFilters(BaseModel):
    category: Optional[str] = Field(None, description="The product category, e.g., 'Smartphone', 'Laptop'.")
    brand: Optional[str] = Field(None, description="The brand of the product, e.g., 'Oppo', 'Lenovo'.")
    min_price: Optional[int] = Field(None, description="The minimum budget in USD.")
    max_price: Optional[int] = Field(None, description="The maximum budget in USD.")
    in_stock: Optional[bool] = Field(True, description="Only return products currently in stock if True.")
    ram: Optional[int] = Field(None, description="Minimum RAM in GB required.")
    storage: Optional[int] = Field(None, description="Minimum storage in GB required.")
    display_type: Optional[str] = Field(None, description="Preferred display type, e.g., 'OLED', 'Retina', 'AMOLED'.")
    soft_filters: Optional[List[str]] = Field(
        None,
        description="List of non-structured preferences derived from description and features, e.g. ['gaming','face unlock']"
    )
    preferences: Optional[str] = Field(None, description="User-specific preferences from profile.")
    interests: Optional[str] = Field(None, description="User-specific interests from profile.")
    tech_savviness: Optional[str] = Field(None, description="User's level of technical expertise.")
