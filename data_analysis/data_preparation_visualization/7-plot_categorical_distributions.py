#!/usr/bin/env python3
"""
Plot Categorical Distributions

Generates bar plots for categorical feature distributions in a grid layout.
"""

import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Visualizes categorical feature distributions.

    Args:
        df: pandas DataFrame
        columns_to_plot: optional list of categorical columns to plot.
                         If None, plots all object dtype columns.

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

    if n_rows == 1:
        axes_list = axes if isinstance(axes, (list, tuple)) else [axes]
    else:
        axes_list = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        ax = axes_list[i]
        counts = df[col].value_counts()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_title(col)
        ax.tick_params(axis='x', rotation=45)

    for j in range(n_features, len(axes_list)):
        axes_list[j].axis('off')

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
