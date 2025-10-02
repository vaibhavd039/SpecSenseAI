import streamlit as st
import pandas as pd

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from pipelines.chains.filter_extraction_chain import product_filter_chain
from pipelines.config import PRODCUCT_DATA_FILE, CUSTOMER_DATA_FILE
from pipelines.utils.data_loader_util import load_data
from pipelines.utils.filter_sanitiser import enrich_filters_from_user_data
from pipelines.utils.data_filter_util import filter_products_using_hard_filters
from pipelines.exceptions import NoRecordsFound, NoMatchingProductsFound
from functools import lru_cache



def retrive_and_sanitise_filtered_products(user_query: str, user_id: str):
    extracted_filters = get_filters(user_query=user_query)
    product_df = load_data(PRODCUCT_DATA_FILE)
    if product_df is None or product_df.empty:
        raise NoRecordsFound("Product Data")
    customer_df = load_data(CUSTOMER_DATA_FILE)
    if customer_df is None or customer_df.empty:
        raise NoRecordsFound("Customer Data")
    enriched_filters = enrich_filters_from_user_data(extracted_filters, user_id=user_id, user_data=customer_df)
    filtered_product_data = filter_products_using_hard_filters( product_df, enriched_filters)
    if filtered_product_data is None or filtered_product_data.empty:
         raise NoMatchingProductsFound()
    filtered_product_data = filtered_product_data.sort_values(by=['rating', 'price'], ascending=[False, True]).head(10)
    return filtered_product_data, enriched_filters

def get_filters(user_query: str):
    chain, format_instructtions = product_filter_chain()
    return chain.invoke({
            "format_instructions": format_instructtions,
            "message": user_query
    })

@lru_cache(1)
def load_customer_data():
    customer_df = load_data(CUSTOMER_DATA_FILE)
    if customer_df is None:
        st.error("Failed to load customer data.")
        return pd.DataFrame()
    return customer_df

@lru_cache(1)
def load_product_data():
    product_df = load_data(PRODCUCT_DATA_FILE)
    if product_df is None:
        st.error("Failed to load product data.")
        return pd.DataFrame()
    return product_df