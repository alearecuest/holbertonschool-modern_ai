#!/usr/bin/env python3
"""
Module to scale numeric features using StandardScaler
"""
from sklearn import preprocessing


def scale_numeric(df):
    """
    Scales MonthlyCharges and TotalCharges using StandardScaler.
    """
    scaler = preprocessing.StandardScaler()
    cols = ['MonthlyCharges', 'TotalCharges']

    if all(col in df.columns for col in cols):
        df[cols] = scaler.fit_transform(df[cols])

    return df
