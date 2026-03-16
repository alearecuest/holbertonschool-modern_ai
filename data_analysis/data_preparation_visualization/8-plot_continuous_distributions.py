#!/usr/bin/env python3
"""
Module to plot continuous distributions
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
    Visualizes the distributions of continuous numerical features.
    """
    if columns_to_plot is None:
        num_cols = df.select_dtypes(include=['number']).columns
        columns_to_plot = num_cols.tolist()
    else:
        columns_to_plot = list(columns_to_plot)

    if not columns_to_plot:
        return

    n_cols = len(columns_to_plot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        ax_hist = axes[i, 0]
        ax_hist.hist(data, bins=30, density=True, alpha=0.7,
                     edgecolor='black', color='steelblue')

        kde = stats.gaussian_kde(data)
        x_vals = np.linspace(data.min(), data.max(), 100)
        ax_hist.plot(x_vals, kde(x_vals), color='red', linestyle='--')
        ax_hist.set_title(f"{col} Histogram + KDE")

        ax_box = axes[i, 1]
        ax_box.boxplot(data, vert=False)
        ax_box.set_title(f"{col} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
