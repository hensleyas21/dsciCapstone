# Data Science Capstone
 
A data science capstone project for Grove City College.

## Authors

Austin Hensley, Stevie Michalik

## Data Sources

[NFL play data](https://github.com/nflverse/nflverse-data/releases/tag/pbp) ([description of the fields](https://www.nflfastr.com/articles/field_descriptions.html))

## Data Cleaning

### Columns Retained

- play_id and game_id: composite unique identifier. Not planning on including in model
- home_team: Categorical. Two or three letter abbreviations of home team
- away_team: Categorical. Two or three letter abbreviations of away team
- season_type: Categorical. Indicator showing if the game was played in the regular or post season
- week: Categorical. Shows what week in the season that it is. Combine with year.
- posteam: Categorical. Two or three letter abbreviation of the team in possession of the ball. Occasionally no values
- posteam_type: Categorical. Indicates whether posteam is home or away  
- defteam: Categorical. Two or three letter abbreviation of the team not in possession of the ball. Occasionally no values
- yardline_100: Nominal. Number of yards away from the goalline that the posteam is. 
- game_date: Categorical. Date the game was played. Not planning on including in model 
- half_seconds_remaining: Nominal. Number of seconds left remaining in the half
- game_seconds_remaining: Nominal. Number of seconds left remaining in the game. 
- game_half: Categorical. Indicates whether the game is in the first or second half
- drive: Nominal. The current drive number for the game. Potentially not including in model
- sp: Categorical. Binary indicator for whether a score occurred on the play. Probably not including in model  
- qtr: Categorical. Indicator 1-4 of what quarter the game is in. 
- down: Categorical. Indicator 1-4 of the down at the beginning of the play  
- goal_to_go: Categorical. Binary indicator showing whether or not the posteam is in a goal to go scenario
- ydstogo: Nominal. Number of yards left until the posteam achieves a first down. 
- ydsnet: Nominal. Numeric value of yards gained on the drive. Probably not including in model.   
- desc: Categorical. Description of the play. Not inlcuding in model  
- play_type: Categorical. Indicates the type of the play including pass (includes sacks), run (includes scrambles), punt, field_goal, kickoff, extra_point, qb_kneel, qb_spike, no_play (timeouts and penalties), and missing for rows indicating end of play. Drop all rows with no value in this column, or no_play  
- yards_gained: Nominal. Number of yards gained on the play.   
- shotgun: Categorical. Binary indicator for whether the posteam was in the shotgun formation  
- no_huddle: Categorical. Binary indicator for whether the posteam did not huddle before the play
- qb_dropback: Categorical. Binary indicator for whether the QB dropped back on the play (pass attempt, sack, or scrambled)  
- qb_scramble: Categorical. Binary indicator for whether the QB scrambled on the play
- air_yards: Nominal. The number of yards the QB threw the ball through the air to the receiver. Probably not feeding into model  
- yards_after_catch: Nominal. The number of yards the receiver carried the ball after the catch. Probably not feeding into model  
- run_location: Categorical. The direction which the ball carrier went on a rush (Left, Middle, Right)  
- run_gap: Categorical. String indicator for line gap of run: end, guard, or tackle  
- field_goal_result: Categorical. String indicator for whether a field goal was made or missed
- kick_distance: Nominal. The distance in yards for a kicking play  
- extra_point_result: Categorical. String indicator showing whether the extra point attempt was successful or not (Good, Failed, Blocked)
- two_point_conv_result: Categorical. String indicator showing whether a two point conversion attempt was successful or not (Success, Failure)
- home_timeouts_remaining: Nominal. Number of timeouts remaining for the home team
- away_timeouts_remaining: Nominal. Number of timeouts remaining for the home team
- timeout: Categorical. Binary indicator showing whether there was timeout taken before the play. Not planning on including in model
- posteam_timeouts_remaining: Nominal. Number of timeouts remaining for the posteam
- defteam_timeouts_remaining: Nominal. Number of timeouts remaining for the defteam  
- posteam_score: Nominal. Number of points which the posteam has before the start of the play.   
- defteam_score: Nominal. Number of points which the defteam has before the start of the play.
- score_differential: Nominal. Difference between the posteam_score and the defteam_score. Not planning on including in model (giving model same data twice)
- posteam_score_post: Nominal. Number of points which the posteam has after the result of the play. Not planning on including in model   
- defteam_score_post: Nominal. Number of points which the defteam has after the result of the play. Not planning on including in model  
- score_differential_post: Nominal. Difference between the posteam_score_post and the defteam_score_post. Not planning on including in model
- epa: Nominal. Expected number of points added by the posteam on the given play. Not planning on including in model
- total_home_rush_epa: Nominal. Total epa up to that point in the game for the home team on rushing plays. Not planning on including in model
- total_away_rush_epa: Nominal. Total epa up to that point in the game for the away team on rushing plays. Not planning on including in model
- total_home_pass_epa: Nominal. Total epa up to that point in the game for the home team on passing plays. Not planning on including in model
- total_away_pass_epa: Nominal. Total epa up to that point in the game for the away team on passing plays. Not planning on including in model
- wp: Nominal. Winning percentage chance for the posteam on the given play. 
- punt_blocked: Categorical. Binary indicator for whether there was a punt block on this play.  
- first_down_rush: Categorical. Binary indicator for whether there was rushing play that went for a first down on this play. 
- first_down_pass: Categorical. Binary indicator for whether there was passing play that went for a first down on this play.  
- first_down_penalty: Categorical. Binary indicator for whether the posteam achieved a first down by penalty
- third_down_converted: Categorical. Binary indicator for whether the posteam converted a third down attempt on this play  
- third_down_failed: Categorical. Binary indicator for whether the posteam failed a third down attempt on this play  
- fourth_down_converted: Categorical. Binary indicator for whether the posteam converted a fourth down attempt on this play
- fourth_down_failed: Categorical. Binary indicator for whether the posteam failed a fourth down attempt on this play
- incomplete_pass: Categorical. Binary indicator for whether a pass was thrown incomplete on this play
- safety: Categorical: Binary indicator for whether a safety occured on this play  
- penalty: Categorical. Binary indicator for whether a penalty occurred on this play  
- fumble_lost: Categorical. Binary indicator for whether a team lost a fumble on this play  
- qb_hit: Categorical. Binary indicator for whether the posteam's QB was hit on the play.   
- rush_attempt: Categorical. Binary indicator for whether the posteam ran a rush play on this play  
- pass_attempt: Categorical. Binary indicator for whether the posteam ran a pass play on this play  
- sack: Categorical. Binary indicator for whether the defteam achieved a sack on this play  
- touchdown: Categorical. Binary indicator for whether a touchdown was scored on this play  
- extra_point_attempt: Categorical. Binary indicator for whether an extra point attempt was made on this play  
- two_point_attempt: Categorical. Binary indicator for whether a two point converstion attempt was made on this play  
- field_goal_attempt: Categorical. Binary indicator for whether a field goal was attempted on this play
- kickoff_attempt: Categorical. Binary indicator for whether a kickoff was attempted on this play  
- punt_attempt: Categorical. Binary indicator for whether a punt was attempted on this play  
- passer_player_id: Categorical. ID to show which player threw a pass on a given play if a pass was thrown
- passer_player_name: Categorical. String to show which player threw a pass on a given play if a pass was thrown  
- passing_yards: Nominal. Number of yards the passer threw for on this play, if a pass was thrown
- receiver_player_id: Categorical. ID to show which player caught a pass on a given play if a pass was thrown
- receiver_player_name: Categorical. String to show which player caught a pass on a given play if a pass was thrown
- receiving_yards: Nominal. Number of yards the receiver had on this play, if a pass was thrown
- rusher_player_id: Categorical. ID to show which player ran the ball on this play, if the play was a run play
- rusher_player_name: Categorical. String to show which player ran the ball on this play, if the play was a run play
- rushing_yards: Nominal. Number of yards the rusher had on this play, if the play was a run  
- kicker_player_id: Categorical. ID to show the player which attempted a kick on this play, if the play was a kicking play  
- kicker_player_name: Categorical. String to show the player which attempted a kick on this play, if the play was a kicking play  
- penalty_team: Categorical. String abbreviation of the team that committed a penalty
- replay_or_challenge: Categorical. Binary indicator for whether the play was replayed or challenged. 
- replay_or_challenge_result: Categorical. String indicating the result of the replay or challenge.   
- season: Categorical. Four-digit number indicating what season the game belongs to
- start_time: Categorical. Kickoff time in eastern time zone.
- stadium: Categorical. Game site name
- weather: Categorical. String describing the weather including temperature, humidity and wind (direction and speed). 
- location: Categorical. Either 'Home' or 'Neutral' indicating if the home team played at home or at a neutral site. 
- div_game: Categorical. Binary indicator for if the given game was a division game.
- roof: Categorical. One of 'dome', 'outdoors', 'closed', 'open' indicating the roof status of the stadium the game was played in. (Source: Pro-Football-Reference)
- surface: Categorical. What type of ground the game was played on. (Source: Pro-Football-Reference)
- temp: Nominal. The temperature at the stadium only for 'roof' = 'outdoors' or 'open'. (Source: Pro-Football-Reference)
- wind: Nominal. The speed of the wind in miles/hour only for 'roof' = 'outdoors' or 'open'. (Source: Pro-Football-Reference)
- home_coach: Categorical. First and last name of home teach coach
- away_coach:  Categorical. First and last name of away teach coach  
