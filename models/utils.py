"""
Utility Functions
=================

This module provides helper functions for parsing data and generating reports.

Author: Khribech Bouchaib
Date: 2024-04-20
Version: 1.0
"""

import pandas as pd
from io import BytesIO

def read_data_file(file_path):
    """
    Reads and parses questionnaire data.
    
    Args:
        file_path (str): Path to the questionnaire file.

    Returns:
        list: Parsed questionnaire groups with questions.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().split("***")
    questions = [{"title": group.split("\n")[0], 
                  "questions": [{"id": f"TRAQ{i+1}", "text": q} 
                                for i, q in enumerate(group.split("\n")[1:])]}
                 for group in content[1].split("\n\n")]
    return questions

def generate_excel_report(user_info, scores):
    """
    Generate an Excel report containing user details and TRAQ scores.

    Args:
        user_info (dict): User demographic information.
        scores (pd.DataFrame): DataFrame of TRAQ scores.

    Returns:
        BytesIO: Buffer containing Excel file.
    """
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        pd.DataFrame([user_info]).to_excel(writer, sheet_name="User Info", index=False)
        scores.to_excel(writer, sheet_name="TRAQ Scores", index=False)
    buffer.seek(0)
    return buffer
