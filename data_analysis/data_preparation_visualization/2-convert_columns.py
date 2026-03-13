#!/usr/bin/env python3
"""
Changing Column Types

- Converts TotalCharges to numeric (non-numeric -> NaN)
- Maps SeniorCitizen from 0/1 to "No"/"Yes"
"""
import pandas as pd


def convert_columns(df):
    """
    Perform type conversion for specific columns.

    Args:
        df (pandas.DataFrame): DataFrame containing 'TotalCharges' and
            'SeniorCitizen' columns.

    Returns:
        pandas.DataFrame: The modified DataFrame.
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

    return df
