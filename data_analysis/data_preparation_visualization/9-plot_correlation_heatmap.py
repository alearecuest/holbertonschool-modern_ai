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

    numeric_df = df.select_dtypes(include=['number'])

    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')

    plt.show()
