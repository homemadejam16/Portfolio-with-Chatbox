

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def show_page():
    st.title("Certifications")
    # Certifications section
    st.header("📜 Certifications")

    # Creating a dataframe for certifications
    certifications_data = {
    "Institution": ["IBM", "DeepLearning.AI", "DeepLearning.AI", "DataCamp"],
    "Certificate": ["IBM Generative AI Engineering Professional Certificate", "Deep Learning Specialization", "Machine Learning Specialization", "Machine Learning Scientist in Python"],
    "Awarded": ["Feb/2025", "Jan/2025", "Jan/2025", "Feb/2025"]
    }

    certifications_df = pd.DataFrame(certifications_data)
    st.table(certifications_df)

