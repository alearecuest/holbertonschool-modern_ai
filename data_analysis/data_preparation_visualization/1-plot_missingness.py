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
    missing = df.isna()
    y, x = np.where(missing)
    plt.plot(x, y, '|')
    plt.yticks(range(df.shape[1]), df.columns)
    plt.show()
