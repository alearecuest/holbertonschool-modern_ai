#!/usr/bin/env python3
"""
Module to plot numeric vs churn
"""
import matplotlib.pyplot as plt
import pandas as pd


def plot_numeric_vs_churn(df, col):
    """
    Compares continuous numeric feature distributions by churn.
    """
    plt.figure(figsize=(12, 8))

    churn_no = df[df['Churn'] == 'No'][col].dropna()
    churn_yes = df[df['Churn'] == 'Yes'][col].dropna()

    plt.hist([churn_no, churn_yes], bins=30, label=['No', 'Yes'])

    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)

    plt.legend(title="Churn")

    plt.savefig("Task_11.png")
    plt.show()
