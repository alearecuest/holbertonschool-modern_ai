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
    Visualizes categorical feature distributions:
    - If columns_to_plot is None, plots all object dtype columns
    - Generates bar plots for each categorical feature in a grid layout
    - Rotates x-axis labels by 45°
    - Displays the plot

    Args:
        df: pandas DataFrame
        columns_to_plot: Optional list of categorical columns
        (default: all object dtype columns)

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

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))

    for i, col in enumerate(columns_to_plot):
        r = i // n_cols
        c = i % n_cols

        if n_rows == 1 and n_cols == 1:
            ax = axes
        elif n_rows == 1:
            ax = axes[c]
        elif n_cols == 1:
            ax = axes[r]
        else:
            ax = axes[r, c]

        counts = df[col].value_counts()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_title(col)
        ax.set_xlabel(col)

        plt.setp(ax.get_xticklabels(), rotation=45)

    total_axes = n_rows * n_cols
    for j in range(n_features, total_axes):
        r = j // n_cols
        c = j % n_cols

        if n_rows == 1 and n_cols == 1:
            ax = axes
        elif n_rows == 1:
            ax = axes[c]
        elif n_cols == 1:
            ax = axes[r]
        else:
            ax = axes[r, c]

        ax.axis('off')

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
