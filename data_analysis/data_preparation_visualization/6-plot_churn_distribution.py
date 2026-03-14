#!/usr/bin/env python3
"""
Plot Target Distribution

Visualize the churn class distribution as a bar plot:
- Uses blue for 'No' and orange for 'Yes'
- Displays the plot
- Returns None
"""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Plot churn value counts.

    Args:
        df: pandas DataFrame with a 'Churn' column

    Returns:
        None
    """
    counts = df['Churn'].value_counts().reindex(['No', 'Yes'])

    plt.figure(figsize=(12, 8))
    plt.bar(['No', 'Yes'], counts.values, color=['blue', 'orange'])
    plt.title('Churn Distribution')
    plt.xlabel('Churn')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
    