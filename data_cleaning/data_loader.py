import numpy as np
import pandas as pd
from numpy.typing import DTypeLike
import glob
import os

def load_data(path: str, columns: dict[str,DTypeLike], missing: dict[str,set[str]]) -> pd.DataFrame:
    """Loads the raw dataset from files using parameters from the config file.

    Positional Arguments:
    path    - The path to the directory or file where your data is located
    columns - The columns from the dataset you plan to use mapped to their data types
    missing - The columns from the dataset mapped to values that indicate data is missing

    returns a DataFrame loaded from the filepath given with the specified columns and types
    """
    csv_files = glob.glob(os.path.join(path, '*.csv'))

    dataframes = []
    for filename in csv_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        dataframes.append(df)
        for column, values in missing.items():
            for value in values:
                df[column] = df[column].replace(value, np.nan)

    df = pd.concat(dataframes, axis=0, ignore_index=True)

    # keep only the columns we want to keep.
    df = df[columns.keys()]

    # for each column we keep, convert the column to numeric or categorical based upon the variable type
    for key, value in columns.items():
        if value == 'real':
            df[key] = pd.to_numeric(df[key], errors='coerce')
        elif value == 'nominal':
            df[key] = df[key].astype('category')

    return df


def save_data(df: pd.DataFrame, path: str) -> None:
    """Saves the transformed dataset into the specified output file"""
    df.to_csv(path, index=False)
