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

    numeric_cols = df.select_dtypes(include=['number'])
    continuous_cols = [c for c in numeric_cols.columns if df[c].nunique() > 10]
    df_continuous = df[continuous_cols]

    corr_matrix = df_continuous.corr()

    sns.heatmap(corr_matrix, 
                annot=True, 
                cmap='coolwarm', 
                vmin=-1, 
                vmax=1)

    plt.title("Correlation Matrix")

    plt.tight_layout()
    plt.show()
