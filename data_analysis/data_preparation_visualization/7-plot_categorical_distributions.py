#!/usr/bin/env python3
"""
Plot Categorical Distributions

Write a function that visualizes categorical feature distributions:
- If columns_to_plot is None, plot all object dtype columns
- Generates bar plots for each categorical feature in a grid layout
- Rotates x-axis labels by 45 degrees
- Saves the plot as Task_7.png and displays it
"""

import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Visualize categorical feature distributions.

    Args:
        df: pandas DataFrame
        columns_to_plot: Optional list of categorical columns (default: all object dtype columns)

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=['object']).columns.tolist()

    n_features = len(columns_to_plot)
    if n_features == 0:
        return

    n_cols = 3
    n_rows = (n_features + n_cols - 1) // n_cols

    plt.figure(figsize=(15, 5 * n_rows))

    for i, col in enumerate(columns_to_plot, start=1):
        plt.subplot(n_rows, n_cols, i)
        df[col].value_counts().plot(kind='bar', rot=45)
        plt.title(col)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
