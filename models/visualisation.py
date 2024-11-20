"""
Visualization Module
====================

This module contains functions for creating diagnostic charts.

Author: Khribech Bouchaib
Date: 2024-04-20
Version: 1.0
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_diagnostic_charts(scores):
    """
    Create bar charts for TRAQ diagnostic results.
    
    Args:
        scores (pd.DataFrame): DataFrame containing TRAQ scores.

    Returns:
        plt.Figure: Figure containing the diagnostic charts.
    """
    # Define chart data
    labels = ["Total", "Attention", "Inhibition"]
    values = scores.iloc[0].tolist()

    # Create the figure
    fig, ax = plt.subplots(figsize=(10, 5))

    # Bar plot
    ax.bar(labels, values, color=["blue", "red", "green"])
    ax.set_title("TRAQ Diagnostic Results")
    ax.set_ylabel("Score")

    return fig
