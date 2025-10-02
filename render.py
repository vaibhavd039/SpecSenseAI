import streamlit as st
import json
import plotly.graph_objects as go

# --- Example function you can replace with your own logic ---
def handle_details(product):
    st.write(f"👉 Showing details for **{product['name']}**")
    # TODO: Add your logic here (API call, navigation, extra UI, etc.)

def create_speedometer(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Score"},
        gauge={'axis': {'range': [0, 100]}}, 
        domain={'row': 0, 'column': 1}
    ))
    fig.update_layout(height=150, margin=dict(l=10,r=10,t=10,b=10))
    return fig

def buld_dashboard(data): 
    # --- FIX 1: Title centered ---
    st.markdown(
        "<h1 style='text-align: center;'>Ranked Products Dashboard - Enhanced Comparison View</h1>", 
        unsafe_allow_html=True
    )

    products = data["ranked_products"]
    product_names = [p['name'] for p in products]

    property_keys = ["score", "hard_matches", "soft_matches", "trade_off", "explanation"]
    property_names = ["Score", "Hard Matches", "Soft Matches", "Trade Off", "Explanation"]

    # --- CSS (keeping your background colors intact) ---
    st.markdown("""
        <style>
            .property-header {
                font-weight: 600; 
                background-color: #f7f9fc; 
                color: #2e475e;
                padding: 12px 10px; 
                border-right: 1px solid #c7d7e3; 
                border-bottom: 1px solid #c7d7e3; 
                text-align: left;
            }
            .score-row .property-header {
                height: 150px; 
                display: flex; align-items: center;
            }
            .product-header {
                font-weight: bold; 
                background-color: #4a7c9d; 
                color: white;
                padding: 15px 10px;
                border-right: 1px solid white; 
                text-align: center;
            }
            .comparison-cell {
                padding: 10px;
                border: none; 
                border-right: 1px solid #e0e0e0; 
                border-bottom: 1px solid #e0e0e0; 
                background-color: white;
                min-height: 100px; 
            }
            .action-row-header {
                min-height: 50px; 
                height: 50px; 
                display: flex;
                align-items: center;
                justify-content: flex-start;
                padding: 0 10px; 
            }
            /* Row background colors preserved */
            .hard-match-bg {background-color: #e6ffe6 !important;}
            .soft-match-bg {background-color: #f0fff0 !important;}
            .trade-off-bg {
                background-color: #fffbe6 !important; 
                border-left: 3px solid #ffcc00; 
                font-style: italic;
            }
            .list-in-cell {margin: 0; padding-left: 20px; line-height: 1.5;}
            .list-in-cell li {margin-bottom: 2px;}
        </style>
    """, unsafe_allow_html=True)

    # --- Column widths (expand all product columns equally) ---
    num_cols = len(products) + 1
    col_widths = [20] + [30] * len(products) 

    # --- Header Row (Product Names) ---
    header_cols = st.columns(col_widths)
    header_cols[0].markdown(
        "<div class='product-header' style='background-color: transparent; border: none;'></div>", 
        unsafe_allow_html=True
    )
    for i, name in enumerate(product_names):
        header_cols[i + 1].markdown(f"<div class='product-header'>{name}</div>", unsafe_allow_html=True)

    # --- Data Rows ---
    for i, key in enumerate(property_keys):
        row_bg_class = ""
        if key == "hard_matches": row_bg_class = " hard-match-bg"
        elif key == "soft_matches": row_bg_class = " soft-match-bg"
        elif key == "trade_off": row_bg_class = " trade-off-bg"
        
        row_class = " score-row" if key == "score" else ""

        row_container = st.container()
        with row_container:
            row_cols = st.columns(col_widths)
            
            # Row header
            row_cols[0].markdown(
                f"<div class='property-header{row_class}'>{property_names[i]}</div>", 
                unsafe_allow_html=True
            )

            for j, product in enumerate(products):
                product_col = row_cols[j + 1]
                cell_class = "comparison-cell" + row_bg_class

                if key == "score":
                    product_col.plotly_chart(
                        create_speedometer(product.get('score', 0)), 
                        use_container_width=True, 
                        key=f"score_gauge_{product['name'].replace(' ', '_')}"
                    )

                elif key in ["hard_matches", "soft_matches", "trade_off"]:
                    content = product.get(key, '-')
                    if key == "trade_off" and isinstance(content, str):
                        content = [content]
                    if isinstance(content, list):
                        list_html = "".join([f"<li>{x}</li>" for x in content])
                        product_col.markdown(
                            f"<div class='{cell_class}'><ul class='list-in-cell'>{list_html}</ul></div>", 
                            unsafe_allow_html=True
                        )
                    else:
                        product_col.markdown(f"<div class='{cell_class}'>{content}</div>", unsafe_allow_html=True)

                elif key == "explanation":
                    product_col.markdown(f"<div class='{cell_class}'>{product.get(key, '-')}</div>", unsafe_allow_html=True)

                else:
                    product_col.markdown(f"<div class='{cell_class}'>{product.get(key, '-')}</div>", unsafe_allow_html=True)

    # --- Final Row: Action Buttons (Option A) ---
    button_row = st.container()
    with button_row:
        row_cols = st.columns(col_widths)

        # Action row header
        row_cols[0].markdown(
            "<div class='property-header action-row-header' style='border-bottom: none;'>Action</div>", 
            unsafe_allow_html=True
        )

        # Buttons in centered flex containers
        for j, product in enumerate(products):
            button_key = f"details_btn_{product['name'].replace(' ', '_')}"
            product_col = row_cols[j + 1]

            product_col.markdown(
                "<div style='display: flex; justify-content: center; align-items: center; height: 100%;'>",
                unsafe_allow_html=True
            )
            if product_col.button("Details", key=button_key):
                handle_details(product)
            product_col.markdown("</div>", unsafe_allow_html=True)
