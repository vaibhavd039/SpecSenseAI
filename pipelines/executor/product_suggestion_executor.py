from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from pipelines.chains.product_suggestion_chain import get_product_suggestion_chain
from pipelines.parser.ranked_product_parser import get_product_ranking_parser
from pipelines.utils.filter_sanitiser import  get_satisfied_hard_filters

def get_top_k_recommendations(enriched_filteres, filtered_product_data, k):
    if filtered_product_data is None or filtered_product_data.empty:
        return []
    chain,format_instructions = get_product_suggestion_chain()
    satisfied_hard_match = get_satisfied_hard_filters(enriched_filteres);
    return chain.invoke({
            "soft_filters": enriched_filteres.soft_filters,
            "preference": enriched_filteres.preferences,
            "interest": enriched_filteres.interests,
            "tech_savviness": enriched_filteres.tech_savviness,
            "hard_filters": satisfied_hard_match,
            "products": filtered_product_data,
            "top_k": k,
            "format_instructions": format_instructions
    })







