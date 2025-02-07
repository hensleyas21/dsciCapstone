# Data Science Capstone
 
A data science capstone project for Grove City College.

## Authors

Austin Hensley, Stevie Michalik

## Data Sources

[NFL play data](https://github.com/nflverse/nflverse-data/releases/tag/pbp) ([description of the fields](https://www.nflfastr.com/articles/field_descriptions.html))

## Data Cleaning

### Columns Retained

- play_id and game_id: composite unique identifier  
- home_team  
- away_team  
- season_type  
- week  
- posteam  
- posteam_type  
- defteam  
- yardline_100  
- game_date  
- half_seconds_remaining  
- game_seconds_remaining  
- game_half  
- quarter_end: drop all rows where value is 1  
- drive  
- sp  
- qtr  
- down  
- goal_to_go  
- ydstogo  
- ydsnet  
- desc  
- play_type: categories including pass (includes sacks), run (includes scrambles), punt, field_goal, kickoff, extra_point, qb_kneel, qb_spike, no_play (timeouts and penalties), and missing for rows indicating end of play. Drop all rows with no value in this column  
- yards_gained  
- shotgun  
- no_huddle  
- qb_dropback  
- qb_scramble  
- pass_location  
- air_yards  
- yards_after_catch  
- run_location  
- run_gap  
- field_goal_result  
- kick_distance  
- extra_point_result  
- two_point_conv_result  
- home_timeouts_remaining  
- away_timeouts_remaining  
- timeout: drop all rows where value is 1  
- posteam_timeouts_remaining  
- defteam_timeouts_remaining  
- posteam_score  
- defteam_score  
- score_differential  
- posteam_score_post  
- defteam_score_post  
- score_differential_post  
- epa  
- total_home_rush_epa  
- total_away_rush_epa  
- total_home_pass_epa  
- total_away_pass_epa  
- wp  
- punt_blocked  
- first_down_rush  
- first_down_pass  
- first_down_penalty  
- third_down_converted  
- third_down_failed  
- fourth_down_converted  
- fourth_down_failed  
- incomplete_pass  
- safety  
- penalty  
- fumble_lost  
- qb_hit  
- rush_attempt  
- pass_attempt  
- sack  
- touchdown  
- extra_point_attempt  
- two_point_attempt  
- field_goal_attempt  
- kickoff_attempt  
- punt_attempt  
- passer_player_id  
- passer_player_name  
- passing_yards  
- receiver_player_id  
- receiver_player_name  
- receiving_yards  
- rusher_player_id  
- rusher_player_name  
- rushing_yards  
- kicker_player_id  
- kicker_player_name  
- penalty_team  
- replay_or_challenge  
- replay_or_challenge_result  
- season  
- series  
- start_time  
- stadium  
- weather  
- play_clock  
- play_deleted  
- play_type_nfl  
- fixed_drive  
- location  
- div_game  
- roof  
- surface  
- temp  
- wind  
- home_coach  
- away_coach  
- play  