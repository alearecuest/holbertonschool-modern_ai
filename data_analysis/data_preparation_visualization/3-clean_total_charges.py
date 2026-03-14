#!/usr/bin/env python3
"""
Dropping vs Replacing vs Imputation

Handle missing values in the TotalCharges column using one of three strategies:
- drop: Remove rows with missing TotalCharges
- median: Fill missing TotalCharges with the column median
- impute: Replace missing TotalCharges with MonthlyCharges * tenure
"""


def clean_total_charges(df, method='drop'):
    """
    Handle missing values in TotalCharges using the specified method.

    Args:
        df: pandas DataFrame containing TotalCharges, MonthlyCharges, and tenure
        method: 'drop', 'median', or 'impute'

    Returns:
        The modified DataFrame (copy).
    """
    if method not in ('drop', 'median', 'impute'):
        raise ValueError("method must be one of: 'drop', 'median', 'impute'")

    df = df.copy()

    if method == 'drop':
        return df.dropna(subset=['TotalCharges'])

    if method == 'median':
        median_val = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median_val)
        return df

    df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges'] * df['tenure'])
    return df
