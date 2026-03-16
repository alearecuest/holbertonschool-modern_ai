#!/usr/bin/env python3
"""
Module to plot categorical distributions
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Visualizes categorical feature distributions:
    - Generates bar plots in a grid
    - Rotates x-axis labels by 45°
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=['object']).columns.tolist()
    else:
        columns_to_plot = list(columns_to_plot)

    n_cols, n_rows = 3, (len(columns_to_plot) + 2) // 3

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
 
    if isinstance(axes, plt.Axes):
        axes = [axes]
    else:
        axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        counts = df[col].value_counts()
        axes[i].bar(counts.index, counts.values)
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)

    for j in range(len(columns_to_plot), len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
