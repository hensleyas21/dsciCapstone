import pandas as pd
import importlib
imported_module = importlib.import_module("additional_cleaning_steps")
importlib.reload(imported_module)
import additional_cleaning_steps

def return_clean_data_df():
    # read in initial data and drop columns not included in the model
    # Note: this is specifically for the model related to predicting play_type.
    cols_to_keep = ['play_type', 'home_team', 'away_team', 'season_type', 'week', 'posteam', 'posteam_type', 'defteam', 'yardline_100',
                    'half_seconds_remaining', 'game_seconds_remaining', 'game_half', 'drive', 'down', 'goal_to_go', 'ydstogo', 'shotgun',
                    'no_huddle', 'posteam_timeouts_remaining', 'defteam_timeouts_remaining', 'posteam_score', 'game_id',
                    'defteam_score', 'score_differential', 'epa', 'wp', 'season', 'stadium', 'location', 'div_game', 'roof', 'surface', 'temp',
                    'wind', 'home_coach', 'away_coach', 'passer_player_name']
    df = pd.read_csv('../cleaned_data.csv')
    df = df.loc[:, cols_to_keep]

    print('apply additional cleaning steps')
    df = additional_cleaning_steps.apply_additional_cleaning(df)

    df = df.drop(columns=['home_coach', 'away_coach', 'game_id'])

    print(f'columns before encoding = {list(df.columns)}')

    one_hot_encoding_fields = ['home_team', 'away_team', 'season_type', 'posteam',
                               'posteam_type', 'defteam', 'game_half', 'stadium', 'location', 'roof',
                               'surface', 'temp', 'wind', 'posteam_coach', 'defteam_coach', 'quarterback_on_field']

    df = pd.get_dummies(df, columns=one_hot_encoding_fields)
    print(f'num cols = {len(df.columns)}')

    return df
