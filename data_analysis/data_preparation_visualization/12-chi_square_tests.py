#!/usr/bin/env python3
"""
Module to perform chi-square tests
"""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Computes the Chi-square p-value to test the independence between
    each categorical feature and the target variable Churn.
    """
    p_values = {}

    for col in df.columns:
        if col in ['Churn', 'customerID']:
            continue

        if df[col].dtype == 'object' or df[col].nunique() < 10:
            contingency_table = pd.crosstab(df[col], df['Churn'])

            chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

            p_values[col] = p

    return p_values
