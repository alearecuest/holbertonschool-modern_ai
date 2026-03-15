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
        columns_to_plot = df.select_dtypes(include=["object"]).columns.tolist()
        grid_cols = 3
    else:
        if isinstance(columns_to_plot, str):
            columns_to_plot = [columns_to_plot]
        else:
            columns_to_plot = list(columns_to_plot)

        grid_cols = 3 if len(columns_to_plot) > 1 else 1

    n_features = len(columns_to_plot)
    if n_features == 0:
        return

    n_cols = min(grid_cols, n_features)
    n_rows = (n_features + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = np.atleast_1d(axes).ravel()

    for i, col in enumerate(columns_to_plot):
        ax = axes[i]
        counts = df[col].value_counts()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_title(col)
        ax.tick_params(axis="x", rotation=45)

    for j in range(n_features, len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
