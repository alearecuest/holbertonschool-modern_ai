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
    bin_cols.append('SeniorCitizen')

    for col in bin_cols:
        if col in df.columns:
            u_vals = set(df[col].dropna().astype(str).unique())
            if u_vals.issubset({'0', '1', '0.0', '1.0'}):
                map_dict = {0: 'No', 1: 'Yes', '0': 'No', '1': 'Yes'}
                df[col] = df[col].map(map_dict)

            df[[col]] = binary_oe.fit_transform(df[[col]])
            df[col] = df[col].astype(int)

    tenure_oe = preprocessing.OrdinalEncoder()
    if 'TenureGroup' in df.columns:
        df[['TenureGroup']] = tenure_oe.fit_transform(df[['TenureGroup']])
        df['TenureGroup'] = df['TenureGroup'].astype(int)

    ohe_cols = ['Contract', 'PaymentMethod']
    exist_ohe = [col for col in ohe_cols if col in df.columns]

    if exist_ohe:
        ohe = preprocessing.OneHotEncoder(drop='first')
        enc_arr = ohe.fit_transform(df[exist_ohe])

        if hasattr(enc_arr, 'toarray'):
            enc_arr = enc_arr.toarray()

        if hasattr(ohe, 'get_feature_names_out'):
            cols = ohe.get_feature_names_out(exist_ohe)
        else:
            cols = ohe.get_feature_names(exist_ohe)

        enc_df = pd.DataFrame(enc_arr, columns=cols, index=df.index)
        enc_df = enc_df.astype(int)

        df = pd.concat([df.drop(columns=exist_ohe), enc_df], axis=1)

    return df, churn_le, binary_oe, tenure_oe
