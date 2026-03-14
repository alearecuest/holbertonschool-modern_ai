#!/usr/bin/env python3
"""
Dropping vs Replacing vs Imputation

Handle missing values in the TotalCharges column using one of three strategies:
- drop:   drop rows where TotalCharges is NaN
- median: fill NaNs with the median of TotalCharges
- impute: fill NaNs with MonthlyCharges * tenure
"""
import pandas as pd


def clean_total_charges(df, method='drop'):
    """
    Handle missing values in TotalCharges using the specified method.

    Args:
        df (pandas.DataFrame): DataFrame containing TotalCharges, MonthlyCharges,
            and tenure.
        method (str): 'drop', 'median', or 'impute'.

    Returns:
        pandas.DataFrame: Modified DataFrame (copy).
    """
    if method not in ['drop', 'median', 'impute']:
        raise ValueError("method must be one of: 'drop', 'median', 'impute'")

    df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        median_val = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median_val)
    else:
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure']
        )

    return df
