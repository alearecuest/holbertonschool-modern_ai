#!/usr/bin/env python3
"""
Module to encode features for modeling using Scikit-learn
"""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    Encodes categorical features into numeric formats suitable for ML modeling.
    """
    churn_le = preprocessing.LabelEncoder()
    if 'Churn' in df.columns:
        df['Churn'] = churn_le.fit_transform(df['Churn']).astype(int)

    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])

    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling']

    for col in binary_cols:
        if col in df.columns:
            df[[col]] = binary_oe.fit_transform(df[[col]]).astype(int)

    if 'SeniorCitizen' in df.columns:
        df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)

    tenure_oe = preprocessing.OrdinalEncoder()
    if 'TenureGroup' in df.columns:
        df[['TenureGroup']] = tenure_oe.fit_transform(
            df[['TenureGroup']]).astype(int)

    ohe_cols = ['Contract', 'PaymentMethod']
    existing_ohe = [col for col in ohe_cols if col in df.columns]

    if existing_ohe:
        ohe = preprocessing.OneHotEncoder(drop='first', sparse_output=False)
        encoded_arrays = ohe.fit_transform(df[existing_ohe])

        encoded_df = pd.DataFrame(
            encoded_arrays,
            columns=ohe.get_feature_names_out(existing_ohe),
            index=df.index
        ).astype(int)

        df = pd.concat([df.drop(columns=existing_ohe), encoded_df], axis=1)

    return df, churn_le, binary_oe, tenure_oe
