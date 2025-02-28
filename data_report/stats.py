import pandas as pd
import os


csv_files = [f for f in os.listdir('data/') if f.endswith(".csv") and f != 'cleaned_data.csv']

id_params = ['play_id', 'game_id']

nominal_params = [
    'play_type', 'home_team', 'away_team', 'season_type', 'week', 'posteam', 'posteam_type',
    'defteam', 'game_half', 'drive', 'sp', 'qtr', 'down', 'goal_to_go', 'shotgun', 
    'no_huddle', 'qb_dropback', 'qb_scramble', 'run_location', 'run_gap', 'field_goal_result', 
    'extra_point_result', 'two_point_conv_result', 'punt_blocked', 'first_down_rush', 
    'first_down_pass', 'first_down_penalty', 'third_down_converted', 'third_down_failed', 
    'fourth_down_converted', 'fourth_down_failed', 'incomplete_pass', 'safety', 'penalty', 'fumble_lost', 
    'qb_hit', 'rush_attempt', 'pass_attempt', 'sack', 'touchdown', 'extra_point_attempt', 
    'two_point_attempt', 'field_goal_attempt', 'kickoff_attempt', 'punt_attempt', 'passer_player_id', 
    'passer_player_name', 'receiver_player_id', 'receiver_player_name', 'rusher_player_id', 
    'rusher_player_name', 'penalty_team', 'replay_or_challenge', 'replay_or_challenge_result', 'season', 
    'start_time', 'stadium', 'weather', 'location', 'div_game', 'roof', 'surface', 'home_coach', 'away_coach'
]

numeric_params = [
    'yardline_100', 'half_seconds_remaining', 'game_seconds_remaining', 'ydstogo', 'yards_gained', 
    'kick_distance', 'home_timeouts_remaining', 'away_timeouts_remaining', 'posteam_timeouts_remaining', 
    'defteam_timeouts_remaining', 'posteam_score', 'defteam_score', 'score_differential', 'epa', 'wp', 
    'passing_yards', 'receiving_yards', 'rushing_yards', 'temp', 'wind'
]

all_params = id_params + nominal_params + numeric_params


# Reads in the CSVs to a DataFrame
if os.path.exists('data_report/data_report_df.pkl'):
    df = pd.read_pickle('data_report/data_report_df.pkl')
else:
    df = pd.DataFrame(columns=all_params)

    for file in csv_files:
        df = pd.concat([df, pd.read_csv(f'data/{file}', usecols=all_params)], axis=0)

    df.to_pickle('data_report/data_report_df.pkl')


# Outputs a CSV with the nominal parameter stats
if not os.path.exists('data_report/nominal_params.csv'):
    nom_df = pd.DataFrame(columns=['param', '%_missing', 'mode', '%_mode'])
    for nom_param in nominal_params:
        mode_val = df[nom_param].mode()[0]
        data = [{
            'param': nom_param,
            '%_missing': df[nom_param].isna().mean(),
            'mode': mode_val,
            '%_mode': (df[nom_param] == mode_val).mean(),
        }]
        nom_df = pd.concat([nom_df, pd.DataFrame(data)], ignore_index=True)

    nom_df.to_csv('data_report/nominal_params.csv')


# Outputs a CSV with the numeric parameter stats
if not os.path.exists('data_report/numeric_params.csv'):
    num_df = pd.DataFrame(columns=['param', '%_missing', 'min', 'max', 'median'])
    for num_param in numeric_params:
        data = [{
            'param': num_param,
            '%_missing': df[num_param].isna().mean(),
            'min': df[num_param].min(),
            'max': df[num_param].max(),
            'median': df[num_param].median(),
        }]
        num_df = pd.concat([num_df, pd.DataFrame(data)], ignore_index=True)

    num_df.to_csv('data_report/numeric_params.csv')