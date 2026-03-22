#!/usr/bin/env python3
"""
Module to plot categorical vs churn
"""
import matplotlib.pyplot as plt
import pandas as pd


def plot_categorical_vs_churn(df, col):
    """
    Visualizes churn rates (Yes proportion) per category as a bar plot.
    """
    churn_crosstab = pd.crosstab(df[col], df['Churn'], normalize='index')

    if 'Yes' in churn_crosstab.columns:
        churn_rates = churn_crosstab['Yes']
    elif 1 in churn_crosstab.columns:
        churn_rates = churn_crosstab[1]
    elif '1' in churn_crosstab.columns:
        churn_rates = churn_crosstab['1']
    else:
        churn_rates = churn_crosstab.iloc[:, -1]

    plt.figure(figsize=(12, 8))

    plt.bar(churn_rates.index.astype(str), churn_rates.values)

    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)

    plt.savefig('Task_10.png')
    plt.show()
