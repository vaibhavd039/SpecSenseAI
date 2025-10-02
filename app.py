import os
import streamlit as st
from utils import init_env
from pipelines.executor import core_executor
import json
import render 
from  pipelines.exceptions  import NoRecordsFound, NoMatchingProductsFound  
init_env()
### STREAMLIT APPLICATION BEGINS

st.set_page_config(page_title="Product Reccomendation Engine", page_icon="")
user_id, user_query = st.columns(2)
with user_id:
    user_id = st.text_input("Enter User Id Please")
with user_query:
    user_query = st.text_area("What are you looking for", height=150)
if st.button("Submit"):
    try:
        respose = core_executor.execute_core_pipeline(user_query= user_query, user_id= user_id, k =3)
        data = json.dumps(respose.model_dump(exclude_none=True))
        render.buld_dashboard(json.loads(data))
    except NoRecordsFound as e:
        st.write(e.message)
    except NoMatchingProductsFound as e:
        st.write(e.message)
    except Exception as e:
        st.write("Something went wrong, please try again later.")