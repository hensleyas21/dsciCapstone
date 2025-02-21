import pandas as pd
from typing import Iterable, Any
from statistics import mode

def fix_missing(df: pd.DataFrame, col_name: str, strategy: str) -> pd.DataFrame:
    """Fixes the missing values in a single column using the specified strategy function.

    Positional Arguments:
    df       - The dataframe on which missing values are to be fixed (may be modified in place)
    col_name - The name of the column whos missing values will be fixed
    strategy - One of the following function names (defined in this file)
                  1. replace_missing_with_mode
                  2. replace_missing_with_mean
                  3. replace_missing_with_median
                  4. replace_missing_with_zero
                  5. replace_missing_with_missing

    returns a reference to the resulting DataFrame (which may be the same as in the input df)
    """
    # identify the correct function to be run on the specified column
    if strategy == 'replace_missing_with_mode': f = replace_missing_with_mode
    elif strategy == 'replace_missing_with_mean': f = replace_missing_with_mean
    elif strategy == 'replace_missing_with_median': f = replace_missing_with_median
    elif strategy == 'replace_missing_with_zero': f = replace_missing_with_zero
    elif strategy == 'replace_missing_with_missing': f = replace_missing_with_missing
    else: raise ValueError(f"Unrecognized missing replacement strategy: {strategy}")
    # call that function and return the resulting DataFrame
    df[col_name] = f(df, col_name)
    return df

def remove_missing(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """Removes all rows from the dataframe where the value in the given column is missing.

    Positional Arguments:
    df       - The dataframe on which missing values are to be removed (may be modified in place)
    col_name - The name of the column whos missing values will be removed

    returns a reference to the resulting DataFrame (which may be the same as in the input df)
    """
    if col_name not in df.columns:
        return df
    return df.copy().dropna(subset=[col_name])

def replace_missing_with_value(df: pd.DataFrame, col_name: str, value: Any) -> Iterable[Any]:
    """Returns a modified version of the given column where missing values are filled with the given static value"""
    if col_name not in df.columns:
        return None
    return df[col_name].fillna(value)

def replace_missing_with_zero(df: pd.DataFrame, col_name: str) -> Iterable[Any]:
    return replace_missing_with_value(df, col_name, 0)

def replace_missing_with_missing(df: pd.DataFrame, col_name: str) -> Iterable[Any]:
    return replace_missing_with_value(df, col_name, "missing")

def replace_missing_with_mode(df: pd.DataFrame, col_name: str) -> Iterable[Any]:
    """Returns a modified version of the given column where missing values are filled with the most common value"""
    if col_name not in df.columns:
        return None
    mode = df[col_name].mode(dropna=True)[0]
    return df[col_name].fillna(mode)

def replace_missing_with_mean(df: pd.DataFrame, col_name: str) -> Iterable[Any]:
    """Returns a modified version of the given column where missing values are filled with the mean value"""
    if col_name not in df.columns:
        return None
    mean = df[col_name].mean(skipna=True)
    return df[col_name].fillna(mean)

def replace_missing_with_median(df: pd.DataFrame, col_name: str) -> Iterable[Any]:
    """Returns a modified version of the given column where missing values are filled with the median value"""
    if col_name not in df.columns:
        return None
    median = df[col_name].median(skipna=True)
    return df[col_name].fillna(median)
