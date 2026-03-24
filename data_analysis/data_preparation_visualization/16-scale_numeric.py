#!/usr/bin/env python3
"""
Module to scale numeric features using StandardScaler
"""
from sklearn import preprocessing


def scale_numeric(df):
    """
    Scales MonthlyCharges and TotalCharges (mean=0, std=1).
    """
    scaler = preprocessing.StandardScaler()
    cols_to_scale = ['MonthlyCharges', 'TotalCharges']

    valid_cols = [col for col in cols_to_scale if col in df.columns]

    if valid_cols:
        df[valid_cols] = scaler.fit_transform(df[valid_cols])

    return df
