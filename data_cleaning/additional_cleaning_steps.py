import pandas as pd
import numpy as np


def apply_additional_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    # For the Coach columns, transform them so that Home Coach and Away Coach are now related to which team is on offense or defense
    if 'home_coach' not in df.columns or 'away_coach' not in df.columns or 'posteam_type' not in df.columns:
        raise Exception('Home and Away coach columns must be present in dataset')

    df['posteam_coach'] = np.where(df['posteam_type'] == 'home', df['home_coach'], df['away_coach'])
    df['defteam_coach'] = np.where(df['posteam_type'] == 'home', df['away_coach'], df['home_coach'])
    df.drop(['home_coach', 'away_coach'], axis=1)

    # For the Passing Player Column, translate it so that passer_player_is applied for all columns (not just pass plays)
    # This ensures that the QB on the field is maintained throughout the whole game.
    # Split each game, and posteam into chunks, forward fill and back fill through each team for the passer player.
    if 'passer_player_name' not in df.columns or 'game_id' not in df.columns:
        raise Exception('passer_player_name needed for transformation')

    grouped = df.groupby(['game_id', 'posteam'])
    chunks = {key: group for key, group in grouped}
    df_list = []

    for key, chunk_df in chunks.items():
        chunk_df['passer_player_name'] = chunk_df['passer_player_name'].replace('missing', np.nan)
        chunk_df['passer_player_name'] = chunk_df['passer_player_name'].ffill().bfill()
        df_list.append(chunk_df)

    new_df = pd.concat(df_list)
    new_df = new_df.rename(columns={'passer_player_name': 'quarterback_on_field'})

    new_df['drive'] = pd.to_numeric(new_df['drive'], errors='coerce').fillna(0)

    return new_df
