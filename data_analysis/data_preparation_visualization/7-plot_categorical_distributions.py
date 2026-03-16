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
        obj_cols = df.select_dtypes(include=['object']).columns
        columns_to_plot = obj_cols.tolist()
    else:
        columns_to_plot = list(columns_to_plot)

    if 'Churn' in columns_to_plot:
        columns_to_plot.remove('Churn')

    n_cols, n_rows = 3, (len(columns_to_plot) + 2) // 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))

    if hasattr(axes, 'flatten'):
        flat_axes = axes.flatten()
    else:
        flat_axes = [axes]

    for i, col in enumerate(columns_to_plot):
        counts = df[col].value_counts()
        flat_axes[i].bar(counts.index, counts.values)
        flat_axes[i].set_title(col)
        flat_axes[i].tick_params(axis='x', rotation=45)

    for j in range(len(columns_to_plot), len(flat_axes)):
        fig.delaxes(flat_axes[j])

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
