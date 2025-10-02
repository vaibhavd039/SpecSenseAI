

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from data_models import ProductFilters
import pandas as pd

def enrich_filters_from_user_data(filters: ProductFilters, user_id: str, user_data: pd.DataFrame) -> ProductFilters:
    if user_data is not None and "user_id" in user_data.columns:
        user_row = user_data[user_data["user_id"] == user_id]
    else:
        user_row = pd.DataFrame()  # or handle appropriately
    if user_row.empty:
        return filters

    user_row = user_row.iloc[0]
    enriched = filters.model_dump(exclude_none=True)

    # 1. Enrich budget from budget_range
    if pd.notna(user_row.get("budget_range")):
        try:
            min_b, max_b = str(user_row["budget_range"]).split("-")
            if filters.min_price is None:
                enriched["min_price"] = int(min_b)
            if filters.max_price is None:
                enriched["max_price"] = int(max_b)
        except Exception:
            pass

    # 2. Enrich preferences, interests, tech_savviness
    for col in ["preferences", "interests", "tech_savviness"]:
        if col in user_row and pd.notna(user_row[col]):
            enriched[col] = str(user_row[col])
    return ProductFilters.model_validate(enriched) if hasattr(ProductFilters, "model_validate") else ProductFilters(**enriched)

def get_satisfied_hard_filters(extracted_filters: ProductFilters) -> dict:
    fields_to_ignore = {'category', 'soft_filters', 'in_stock'}
    collected_dict = extracted_filters.model_dump(
        exclude=fields_to_ignore,
        exclude_none=True
    )
    print(collected_dict)
    return collected_dict