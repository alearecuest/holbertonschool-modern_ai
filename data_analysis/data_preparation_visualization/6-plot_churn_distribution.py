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
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts().reindex(['No', 'Yes'])
    ax = counts.plot(kind='bar', color=['blue', 'orange'])

    ax.set_title('Churn Distribution')
    ax.set_xlabel('Churn')
    ax.set_ylabel('Count')

    plt.tight_layout()
    plt.show()
