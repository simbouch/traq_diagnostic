"""
Traq Diagnostic Application
===========================

This application helps in the diagnosis of behavioral and attention disorders
based on TRAQ scores and visualizes the diagnostic data.

Author: Khribech Bouchaib
Date: 2024-04-20
Version: 1.0
"""

# Import necessary libraries
import streamlit as st
import pandas as pd
from io import BytesIO
from models.traq_model import calculate_traq_scores
from models.visualization import plot_diagnostic_charts
from models.utils import read_data_file, generate_excel_report

# Configure Streamlit
st.set_page_config(layout="wide")
st.title("Traq Diagnostic Application")

# Sidebar: Collect demographic information
st.sidebar.header("User Information")
user_info = {
    "lastName": st.sidebar.text_input("Last Name"),
    "firstName": st.sidebar.text_input("First Name"),
    "birthDate": st.sidebar.date_input("Date of Birth"),
    "sex": st.sidebar.selectbox("Gender", ["Male", "Female"]),
    "educationLevel": st.sidebar.selectbox(
        "Education Level",
        ["CAP/BEP", "Professional Baccalaureate", "General Baccalaureate", 
         "Bac +2 (DUT/BTS)", "Bac +3 (License)", "Bac +5 (Master)", "Bac +7 (Doctorate)"]
    ),
}

# Add an image in the sidebar
st.sidebar.image("static/images/clinicog.png", width=200)

# Load questionnaire data
questions = read_data_file("data/questionnaire.txt")

# Main Content: Display questionnaire
st.write("## TRAQ Questionnaire")
answers = {}
for group in questions:
    st.write(f"### {group['title']}")
    for q in group['questions']:
        answers[q['id']] = st.slider(q['text'], min_value=1, max_value=5, step=1)

# Save and analyze data on button click
if st.button("Save and Analyze"):
    # Convert answers to a DataFrame
    answers_df = pd.DataFrame([answers])

    # Calculate TRAQ scores
    traq_scores = calculate_traq_scores(answers_df)

    # Visualize diagnostic results
    fig = plot_diagnostic_charts(traq_scores)
    st.pyplot(fig)

    # Generate downloadable report
    report_buffer = generate_excel_report(user_info, traq_scores)
    st.download_button(
        label="Download Report",
        data=report_buffer,
        file_name=f"{user_info['lastName']}_traq_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
