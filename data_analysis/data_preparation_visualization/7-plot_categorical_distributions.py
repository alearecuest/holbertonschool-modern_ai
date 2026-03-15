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
    if axes is None:
        return []
    # scalar Axes
    if not hasattr(axes, "__len__") or isinstance(axes, plt.Axes):
        return [axes]
    # numpy-like arrays or lists of lists
    flat = []
    try:
        for ax in axes:
            if hasattr(ax, "__len__") and not isinstance(ax, plt.Axes):
                flat.extend(list(ax))
            else:
                flat.append(ax)
        return flat
    except TypeError:
        return [axes]


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Visualizes categorical feature distributions.

    Args:
        df: pandas DataFrame
        columns_to_plot: Optional list of categorical columns
                         (default: all object dtype columns)

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=["object"]).columns.tolist()
        n_cols = 3
    else:
        if isinstance(columns_to_plot, str):
            columns_to_plot = [columns_to_plot]
        else:
            try:
                columns_to_plot = list(columns_to_plot)
            except TypeError:
                columns_to_plot = [columns_to_plot]
        n_cols = 3

    columns_to_plot = [c for c in columns_to_plot if c in df.columns]

    n_features = len(columns_to_plot)
    if n_features == 0:
        return

    n_cols = min(n_cols, n_features)
    n_rows = (n_features + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes_list = _flatten_axes(axes)

    for i, col in enumerate(columns_to_plot):
        ax = axes_list[i]
        counts = df[col].value_counts()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_title(col)
        ax.tick_params(axis="x", rotation=45)

    for j in range(n_features, len(axes_list)):
        try:
            axes_list[j].axis("off")
        except Exception:
            pass

    plt.tight_layout()
    try:
        plt.savefig("Task_7.png")
    except Exception:
        pass
    plt.show()
