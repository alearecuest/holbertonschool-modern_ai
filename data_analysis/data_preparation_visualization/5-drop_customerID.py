#!/usr/bin/env python3
"""
5. Initial Dropping

Remove the customerID column from the DataFrame since unique identifiers
generally lack predictive value.
"""


def drop_customerID(df):
    """
    Drop the customerID column.

    Args:
        df: pandas DataFrame containing a 'customerID' column

    Returns:
        DataFrame without the 'customerID' column
    """
    return df.drop(columns=['customerID'])
