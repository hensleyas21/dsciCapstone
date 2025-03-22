import pandas as pd

def return_clean_data_df():
    # read in initial data and drop columns not included in the model
    # Note: this is specifically for the model related to predicting play_type.
    cols_to_keep = ['play_type', 'season_type', 'week', 'posteam', 'posteam_type', 'defteam', 'yardline_100',
                    'half_seconds_remaining', 'game_seconds_remaining', 'game_half', 'drive', 'down', 'goal_to_go', 'ydstogo', 'shotgun',
                    'no_huddle', 'posteam_timeouts_remaining', 'defteam_timeouts_remaining', 'posteam_score',
                    'defteam_score', 'score_differential', 'wp', 'season', 'location', 'div_game', 'roof', 'surface', 'temp',
                    'wind', 'quarterback_on_field', 'posteam_coach', 'defteam_coach']
    df = pd.read_csv('../cleaned_data.csv')
    df = df.loc[:, cols_to_keep]

    print(f'columns before encoding = {list(df.columns)}')

    one_hot_encoding_fields = ['season_type', 'posteam', 'posteam_type', 'defteam', 'game_half', 'location', 'roof',
                               'surface', 'temp', 'wind', 'posteam_coach', 'defteam_coach', 'quarterback_on_field']

    df = pd.get_dummies(df, columns=one_hot_encoding_fields)
    print(f'num cols = {len(df.columns)}')

    return df
