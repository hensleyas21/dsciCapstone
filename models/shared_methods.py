import pandas as pd
import additional_cleaning_steps

def return_clean_data_df():
    # read in initial data and drop columns not included in the model
    # Note: this is specifically for the model related to predicting play_type.
    cols_to_keep = ['play_type', 'home_team', 'away_team', 'season_type', 'week', 'posteam', 'posteam_type', 'defteam', 'yardline_100',
                    'half_seconds_remaining', 'game_seconds_remaining', 'game_half', 'drive', 'qtr', 'down', 'goal_to_go', 'ydstogo', 'shotgun',
                    'no_huddle', 'posteam_timeouts_remaining', 'defteam_timeouts_remaining', 'posteam_score',
                    'defteam_score', 'score_differential','epa', 'wp', 'season', 'start_time', 'stadium', 'location', 'div_game', 'roof', 'surface', 'temp',
                    'wind', 'home_coach', 'away_coach']
    df = pd.read_csv('../cleaned_data.csv')
    df = df.loc[:, cols_to_keep]

    print('apply additional cleaning steps')
    df = additional_cleaning_steps.apply_additional_cleaning(df)

    print(f'columns before encoding = {list(df.columns)}')

    one_hot_encoding_fields = ['home_team', 'away_team', 'season_type', 'posteam', 'drive',
                               'posteam_type', 'defteam', 'game_half', 'start_time', 'stadium', 'location', 'roof',
                               'surface', 'temp', 'wind', 'posteam_coach', 'defteam_coach']

    df = pd.get_dummies(df, columns=one_hot_encoding_fields)
    print(f'num cols = {len(df.columns)}')

    return df
