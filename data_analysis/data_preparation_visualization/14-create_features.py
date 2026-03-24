#!/usr/bin/env python3
"""
Module to create new features: NumServices and TenureGroup
"""
import pandas as pd


def create_features(df):
    """
    Engineers new features from the dataset and drops original columns.
    """
    service_cols = [
        'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies'
    ]

    existing_services = [col for col in service_cols if col in df.columns]

    df['NumServices'] = 0

    for col in existing_services:
        if col == 'InternetService':
            df['NumServices'] += df[
                col].isin(['DSL', 'Fiber optic']).astype(int)
        else:
            df['NumServices'] += (df[col] == 'Yes').astype(int)

    bins = [-1, 12, 24, 48, 60, float('inf')]
    labels = ['0-12', '13-24', '25-48', '49-60', '60+']

    if 'tenure' in df.columns:
        df['TenureGroup'] = pd.cut(df['tenure'], bins=bins, labels=labels)

    cols_to_drop = existing_services + ['tenure']
    cols_to_drop = [c for c in cols_to_drop if c in df.columns]

    df.drop(columns=cols_to_drop, inplace=True)

    return df
