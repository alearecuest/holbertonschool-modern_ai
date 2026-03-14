#!/usr/bin/env python3
"""
Plot Categorical Distributions

Generates bar plots for categorical feature distributions in a grid layout.
"""

import matplotlib.pyplot as plt
import numpy as np

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
    axes = np.array(axes).reshape(-1)

    for i, col in enumerate(columns_to_plot):
        ax = axes[i]
        df[col].value_counts().plot(kind='bar', ax=ax, rot=45)
        ax.set_title(col)

    for j in range(n_features, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
