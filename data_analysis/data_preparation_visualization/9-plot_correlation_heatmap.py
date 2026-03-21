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
    if 'SeniorCitizen' in numeric_df.columns:
        numeric_df = numeric_df.drop(columns=['SeniorCitizen'])

    corr_matrix = numeric_df.corr()

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

    plt.show()
