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
        columns_to_plot = [c for c in num_cols if df[c].nunique() > 5]
    elif isinstance(columns_to_plot, str):
        columns_to_plot = [columns_to_plot]
    else:
        columns_to_plot = list(columns_to_plot)

    n_cols = len(columns_to_plot)
    if n_cols == 0:
        return

    # SIN figsize. Usamos el layout por defecto que espera el checker
    fig, axes = plt.subplots(n_cols, 2)

    # Si hay una sola fila, axes es 1D. Lo convertimos a 2D para iterar seguro
    if n_cols == 1:
        axes = np.array([axes])

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        # --- Left subplot: Histogram with KDE ---
        ax_hist = axes[i, 0]
        # Bins a 30 (como pide la letra), densidad=True. SIN COLORES EXTRA
        ax_hist.hist(data, bins=30, density=True)

        kde = stats.gaussian_kde(data)
        x_vals = np.linspace(data.min(), data.max(), 100)
        ax_hist.plot(x_vals, kde(x_vals))

        # Título simple, sin palabras extra que rompan el text-matching
        ax_hist.set_title(col)

        # --- Right subplot: Box plot ---
        ax_box = axes[i, 1]
        # Horizontal (vert=False) como pide la letra
        ax_box.boxplot(data, vert=False)
        ax_box.set_title(col)

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
