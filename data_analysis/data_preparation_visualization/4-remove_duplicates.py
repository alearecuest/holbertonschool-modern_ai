#!/usr/bin/env python3
"""
Removing Duplicates

Remove duplicate rows from a DataFrame, printing duplicates (if any) and the
duplicate counts before and after removal.
"""


def remove_duplicates(df):
    """
    Print duplicates (if any), show counts before/after, drop duplicates,
    and return the deduplicated DataFrame.

    Args:
        df: pandas DataFrame to process

    Returns:
        Deduplicated DataFrame
    """
    return df.drop_duplicates()