#!/usr/bin/env python3
"""
Module to plot categorical distributions
"""
import matplotlib.pyplot as plt
import math


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Visualizes categorical feature distributions:
    - Generates bar plots in a grid
    - Rotates x-axis labels by 45°
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=['object']).columns.tolist()
    
    if not columns_to_plot:
        return

    n_cols = 3 
    n_rows = math.ceil(len(columns_to_plot) / n_cols) 
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    
    axes = axes.flatten() if isinstance(axes, (list, tuple)) or hasattr(axes, 'flatten') else [axes]

    for i, col in enumerate(columns_to_plot):
        value_counts = df[col].value_counts()
        
        axes[i].bar(value_counts.index.astype(str), value_counts.values, color='#4C72B0')
        
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)

    for j in range(len(columns_to_plot), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
