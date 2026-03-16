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
        columns_to_plot = [col for col in df.columns if df[col].dtype == 'object' and col != 'Churn']
    elif isinstance(columns_to_plot, str):
        columns_to_plot = [columns_to_plot]
    else:
        columns_to_plot = list(columns_to_plot)

    n_features = len(columns_to_plot)
    if n_features == 0:
        return

    n_cols = 3
    n_rows = (n_features + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))

    if n_rows == 1:
        axes = [axes]
    if n_cols == 1:
        axes = [[ax] for ax in axes]

    for idx, col in enumerate(columns_to_plot):
        r = idx // n_cols
        c = idx % n_cols
        ax = axes[r][c]
        vc = df[col].value_counts()
        ax.bar(vc.index.astype(str), vc.values)
        ax.set_xlabel(col)
        plt.setp(ax.get_xticklabels(), rotation=45)

    for idx in range(n_features, n_rows * n_cols):
        r = idx // n_cols
        c = idx % n_cols
        axes[r][c].axis('off')

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()