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

    fig, ax = plt.subplots(figsize=(12, 8))
    counts.plot(kind='bar', ax=ax, color=['tab:blue', 'tab:orange'], rot=0)

    ax.set_title('Churn Distribution')
    ax.set_ylabel('Count')

    plt.show()
