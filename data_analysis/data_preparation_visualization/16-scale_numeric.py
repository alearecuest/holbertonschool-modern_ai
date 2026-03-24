#!/usr/bin/env python3
"""
Module to scale numeric features using StandardScaler
"""
from sklearn import preprocessing


def scale_numeric(df):
    """
    Scales numeric columns using StandardScaler.
    """
    scaler = preprocessing.StandardScaler()

    cols = ['MonthlyCharges', 'TotalCharges']

    for col in cols:
        if col in df.columns:
            df[[col]] = scaler.fit_transform(df[[col]])

    return df
