import pandas as pd
import numpy as np


def apply_additional_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    # For the Coach columns, transform them so that Home Coach and Away Coach are now related to which team is on offense or defense
    if 'home_coach' not in df.columns or 'away_coach' not in df.columns or 'posteam_type' not in df.columns:
        raise Exception('Home and Away coach columns must be present in dataset')

    df['posteam_coach'] = np.where(df['posteam_type'] == 'home', df['home_coach'], df['away_coach'])
    df['defteam_coach'] = np.where(df['posteam_type'] == 'home', df['away_coach'], df['home_coach'])
    df.drop(['home_coach', 'away_coach'], axis=1)

    return df
