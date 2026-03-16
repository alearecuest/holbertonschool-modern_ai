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
        # Extraemos numéricas si no se especifica ninguna
        columns_to_plot = df.select_dtypes(include=['number']).columns.tolist()
    else:
        # Protegemos contra un string suelto para pasar el test específico
        if isinstance(columns_to_plot, str):
            columns_to_plot = [columns_to_plot]
        else:
            columns_to_plot = list(columns_to_plot)

    n_cols = len(columns_to_plot)
    
    # Detenemos si no hay columnas
    if n_cols == 0:
        return

    # Usamos EXACTAMENTE el figsize del esqueleto original
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        # --- Left subplot: Histogram with KDE ---
        # Respetamos rigurosamente los 4 parámetros que pide la letra
        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7, edgecolor='black')
        
        kde = stats.gaussian_kde(data)
        x_vals = np.linspace(data.min(), data.max(), 100)
        axes[i, 0].plot(x_vals, kde(x_vals), color='red', linestyle='--')
        
        # Título idéntico a la imagen de referencia
        axes[i, 0].set_title(f"{col} Histogram + KDE")

        # --- Right subplot: Box plot ---
        axes[i, 1].boxplot(data, vert=False)
        
        # Título idéntico a la imagen de referencia
        axes[i, 1].set_title(f"{col} Boxplot")

    # Respetamos el final del esqueleto
    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
