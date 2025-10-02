from pipelines.executor.filter_extraction_executor import retrive_and_sanitise_filtered_products
from pipelines.executor.product_suggestion_executor import get_top_k_recommendations

def execute_core_pipeline(user_query: str, user_id: str, k: int):
    filtered_product_data, enriched_filters = retrive_and_sanitise_filtered_products(user_query, user_id)
    return get_top_k_recommendations(enriched_filters, filtered_product_data, k)
    