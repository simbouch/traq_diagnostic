"""
TRAQ Model
==========

This module provides calculations for TRAQ scores, including metrics for 
attention, inhibition, and total scores.

Author: Khribech Bouchaib
Date: 2024-04-20
Version: 1.0
"""

import pandas as pd

def calculate_traq_scores(answers: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate TRAQ scores based on questionnaire answers.
    
    Args:
        answers (pd.DataFrame): DataFrame containing TRAQ-related responses.

    Returns:
        pd.DataFrame: DataFrame containing calculated TRAQ scores.
    """
    attention = ['TRAQ1', 'TRAQ2', 'TRAQ4', 'TRAQ8', 'TRAQ10']
    inhibition = ['TRAQ3', 'TRAQ5', 'TRAQ6', 'TRAQ7', 'TRAQ9']
    scores = pd.DataFrame()

    scores['attention'] = answers[attention].sum(axis=1)
    scores['inhibition'] = answers[inhibition].sum(axis=1)
    scores['total'] = scores[['attention', 'inhibition']].sum(axis=1)

    return scores
