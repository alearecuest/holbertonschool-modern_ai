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

    miss = df.isna().to_numpy()
    rows, cols = np.where(miss)

    plt.scatter(rows, cols, marker='|', s=200, color='tab:blue')
    plt.xlabel("Row index")
    plt.ylabel("Columns")
    plt.yticks(range(df.shape[1]), df.columns)
    plt.title("Missingness Plot")
    plt.tight_layout()

    plt.savefig("Figure_1.png")
    plt.close()
