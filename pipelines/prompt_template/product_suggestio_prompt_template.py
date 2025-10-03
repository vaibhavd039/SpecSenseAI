def get_ranking_prompt():
    from langchain_core.prompts import ChatPromptTemplate
    ranking_prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an assistant that ranks products for a user's request. You need to internally use "
            "chain-of-thought style reasoning to compare and evaluate products, but UNDER NO CIRCUMSTANCE "
            "should you output step-by-step chain-of-thought. Only produce the final structured JSON described below."
        )),
        ("user", (
             "Soft filters: {soft_filters}\n\n"
             "User Preference: {preference}\n\n"
             "User Interest: {interest}\n\n"
             "Tech Savviness: {tech_savviness}\n\n"
             "Extracted Hard Filters: {hard_filters}\n\n"
             "Here are the filtered products:\n{products}\n\n"
             "- top_k: {top_k}\n\n"
            
            "Task:\n"
            "1) Rank the products according to how well they match the SOFT preferences (soft_filters) and since all {hard_filters} are already satisfied just mention those"
            "2) If Provided, consider User Preference, Tech Savviness and User Interest to rank those products and provide score out of 100."
            "2) If no products fully satisfy, suggest alternatives and list violated soft filters.\n\n"
            "3) Return satisfied hard_matches, soft_matches, trade-offs, unmet needs in more human readable form.\n\n"
            "Output format requirement:\n"
            "{format_instructions}\n\n"
        ))
    ])
    return ranking_prompt