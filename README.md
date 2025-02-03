# Data Science Capstone
 
A data science capstone project for Grove City College.

## Authors

Austin Hensley, Stevie Michalik

## Data Sources

[NFL play data](https://github.com/nflverse/nflverse-data/releases/tag/pbp) ([description of the fields](https://www.nflfastr.com/articles/field_descriptions.html))

## Data Cleaning

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

TODO: start from no_score_prob