#!/usr/bin/env python3
"""
Visualize Missing Data
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Visualize missing values in a DataFrame as vertical bars (|).

    Saves the plot as Figure_1.png (headless-friendly).
    """
    plt.figure(figsize=(12, 8))
    x, y = np.where(df.isna())
    plt.scatter(x, y, marker='|')
    plt.yticks(range(df.shape[1]), df.columns)
    plt.gca().invert_yaxis()
    plt.show()
