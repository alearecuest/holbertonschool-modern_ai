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
        columns_to_plot = df.select_dtypes(include=['number']).columns.tolist()
    else:
        if isinstance(columns_to_plot, str):
            columns_to_plot = [columns_to_plot]
        else:
            columns_to_plot = list(columns_to_plot)

    n_cols = len(columns_to_plot)
    if n_cols == 0:
        return

    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7, edgecolor='black')

        kde = stats.gaussian_kde(data)
        x_vals = np.linspace(data.min(), data.max(), 100)
        axes[i, 0].plot(x_vals, kde(x_vals), color='red', linestyle='--')

        axes[i, 0].set_title(f"{col} Histogram + KDE")

        axes[i, 1].boxplot(data, vert=False)
        axes[i, 1].set_title(f"{col} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
