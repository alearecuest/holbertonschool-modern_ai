#!/usr/bin/env python3
"""
Module to encode features for modeling using Scikit-learn
"""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    Encodes categorical features into numeric formats suitable for ML.
    """
    churn_le = preprocessing.LabelEncoder()
    if 'Churn' in df.columns:
        df['Churn'] = churn_le.fit_transform(df['Churn']).astype(int)

    cats = [['No', 'Yes']]
    binary_oe = preprocessing.OrdinalEncoder(categories=cats)

    bin_cols = ['Partner', 'Dependents', 'PaperlessBilling']

    for col in bin_cols:
        if col in df.columns:
            df[[col]] = binary_oe.fit_transform(df[[col]]).astype(int)

    if 'SeniorCitizen' in df.columns:
        df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)

    tenure_oe = preprocessing.OrdinalEncoder()
    if 'TenureGroup' in df.columns:
        t_group = df[['TenureGroup']]
        df[['TenureGroup']] = tenure_oe.fit_transform(t_group).astype(int)

    ohe_cols = ['Contract', 'PaymentMethod']
    exist_ohe = [col for col in ohe_cols if col in df.columns]

    if exist_ohe:
        ohe = preprocessing.OneHotEncoder(drop='first', sparse_output=False)
        enc_arr = ohe.fit_transform(df[exist_ohe])

        col_names = ohe.get_feature_names_out(exist_ohe)

        enc_df = pd.DataFrame(enc_arr, columns=col_names, index=df.index)
        enc_df = enc_df.astype(int)

        df = pd.concat([df.drop(columns=exist_ohe), enc_df], axis=1)

    return df, churn_le, binary_oe, tenure_oe
