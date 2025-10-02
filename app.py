import os
import streamlit as st
from utils import init_env
from pipelines.executor import core_executor
import json
import render 
from  pipelines.exceptions  import NoRecordsFound, NoMatchingProductsFound  
init_env()
### STREAMLIT APPLICATION BEGINS


# --- Configuration ---
st.set_page_config(layout="centered", page_title="Stylish Input Form - Right-Shifted Button")

# --- Custom CSS and HTML ---
custom_css_html = """
<style>
    /* Main container styling */
    .form-container {
        background-color: #f7f9fb;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 500px;
        margin: 0 auto;
        border-top: 5px solid #4a90e2;
    }

    /* Styling for the form title */
    .form-title {
        color: #333;
        text-align: center;
        margin-bottom: 25px;
        font-size: 1.8em;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Input Styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        width: 100%;
        padding: 10px 15px;
        border: 1px solid #ddd;
        border-radius: 8px;
        transition: all 0.3s ease;
        box-sizing: border-box;
    }

    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #4a90e2;
        box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
        outline: none;
    }

    /* Button Styling */
    .stButton button {
        /* Set a fixed width to allow centering within the column */
        width: 200px !important;
        padding: 12px !important;
        border: none !important;
        border-radius: 8px !important;
        background-color: #4a90e2 !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.1em !important;
        cursor: pointer !important;
        transition: background-color 0.3s ease, transform 0.1s ease !important;
        
        /* Centering the button within the column */
        display: block !important;
        margin-left: auto !important; /* This ensures the button aligns to the right side of its column */
        margin-right: 0 !important;
    }

    .stButton button:hover {
        background-color: #3a7fd0 !important;
    }
</style>

<div class="form-container">
    <h2 class="form-title"> 📲 🔎 Gadget-Saathi 🔎 💻 </h2>
"""

# Close the HTML div after the Streamlit elements
html_close = """
</div>
"""

# Inject the custom styling and the opening container
st.markdown(custom_css_html, unsafe_allow_html=True)

# --- Streamlit Form Logic ---
with st.form("user_input_form"):
    # 1. UserID Input
    user_id = st.text_input(
        "User ID",
        key="user_id_input",
        placeholder="e.g., U12345",
        label_visibility="visible"
    )

    # 2. User Query Input
    user_query = st.text_area(
        "User Query",
        key="user_query_input",
        placeholder="Enter your detailed query here...",
        label_visibility="visible",
        height=150
    )

    # 3. Submit Button - Shifted Right Solution
    # Column ratios: [Left Empty Space, Button Column, Right Empty Space]
    # [1, 1.5, 0.5] makes the left space larger, pushing the content (button) to the right.
    col1, col2, col3 = st.columns([1, 1.5, 0.5])

    with col2:
        # We also adjust the CSS within this column to ensure right-alignment for maximum shift.
        submitted = st.form_submit_button("Submit Query")

# Inject the closing HTML container
st.markdown(html_close, unsafe_allow_html=True)

# --- Display Submission Result (Optional) ---
if submitted:
    try:
        respose = core_executor.execute_core_pipeline(user_query= user_query, user_id= user_id, k =3)
        data = json.dumps(respose.model_dump(exclude_none=True))
        render.buld_dashboard(json.loads(data))
    except Exception as e:
        st.write(str(e))