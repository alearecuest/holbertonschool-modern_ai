#!/usr/bin/env python3
"""
Module to perform Welch's t-tests for numeric features
"""
from scipy import stats


def ttest_numeric(df):
    """
    Computes t-test p-value comparing Churn=Yes vs Churn
    =No for each numeric feature using Welch's t-test.
    """
    p_values = {}

    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        if col in ['SeniorCitizen', 'customerID', 'Churn']:
            continue

        churn_yes = df[df['Churn'] == 'Yes'][col].dropna()
        churn_no = df[df['Churn'] == 'No'][col].dropna()

        t_stat, p_val = stats.ttest_ind(churn_yes, churn_no, equal_var=False)

        p_values[col] = p_val

    return p_values
