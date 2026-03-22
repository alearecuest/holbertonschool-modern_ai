#!/usr/bin/env python3
"""
Module to plot correlation heatmap
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Visualizes correlations between continuous numeric features using seaborn.
    """
    plt.figure(figsize=(6, 5))

    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    if 'SeniorCitizen' in num_cols:
        num_cols.remove('SeniorCitizen')

    corr_matrix = df[num_cols].corr()

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

    plt.show()
