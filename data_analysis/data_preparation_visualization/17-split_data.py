#!/usr/bin/env python3
"""
Module to split data into train and test sets with stratified sampling
"""
import pandas as pd
from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """
    Splits data into train/test sets preserving class distribution.
    """
    if target not in df.columns:
        return None, None, None, None

    X = df.drop(columns=[target])
    y = df[target]

    X_tr, X_te, y_tr, y_te = model_selection.train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    return X_tr, X_te, y_tr, y_te
