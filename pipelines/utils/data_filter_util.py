
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from data_models import ProductFilters
import pandas as pd


def filter_products_using_hard_filters(df: pd.DataFrame, filters: ProductFilters) -> pd.DataFrame:
    filtered_df = df.copy()
    if filters.category:
        filtered_df = filtered_df[filtered_df["category"].str.lower() == filters.category.lower()]
    if filters.brand:
        filtered_df = filtered_df[filtered_df["brand"].str.lower() == filters.brand.lower()]
    if filters.min_price is not None:
        filtered_df = filtered_df[filtered_df["price"] >= filters.min_price]
    if filters.max_price is not None:
        filtered_df = filtered_df[filtered_df["price"] <= filters.max_price]
    if filters.in_stock:
        filtered_df = filtered_df[filtered_df["stock_count"] > 0]
    if filters.ram:
        filtered_df = filtered_df[filtered_df["specifications"].str.contains(
            f"RAM: {filters.ram}", case=False, na=False)]
    if filters.storage:
        filtered_df = filtered_df[filtered_df["specifications"].str.contains(
            f"Storage: {filters.storage}", case=False, na=False)]
    if filters.display_type:
        filtered_df = filtered_df[filtered_df["specifications"].str.contains(
            filters.display_type, case=False, na=False)]
    return filtered_df