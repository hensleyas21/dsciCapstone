# Analyzing NFL Data
 
A data science capstone project for Grove City College. This project aims to anaylze a variety of data from the NFL and to create a model to predict different play types.

## Authors

[Austin Hensley](https://austinhensley.com),
[Stevie Michalik](https://github.com/MichalikSJ21)

## Data Sources

[NFL Play Data](https://github.com/nflverse/nflverse-data/releases/tag/pbp)[^1]

## Data Cleaning

To clean the data, run the following command from the main directory of the project:  
```sh
py data_cleaning/demo.py data_cleaning/config.json
```

### Columns Retained

- play_id and game_id: composite unique identifier. Not planning on including in model
- play_type: Categorical. Indicates the type of the play including pass (includes sacks), run (includes scrambles), punt, field_goal, kickoff, extra_point, qb_kneel, qb_spike, no_play (timeouts and penalties), and missing for rows indicating end of play. Drop all rows with no value in this column, or no_play
- home_team: Categorical. Two or three letter abbreviations of home team
- away_team: Categorical. Two or three letter abbreviations of away team
- season_type: Categorical. Indicator showing if the game was played in the regular or post season
- week: Categorical. Shows what week in the season that it is. Combine with year.
- posteam: Categorical. Two or three letter abbreviation of the team in possession of the ball. Occasionally no values
- posteam_type: Categorical. Indicates whether posteam is home or away  
- defteam: Categorical. Two or three letter abbreviation of the team not in possession of the ball. Occasionally no values
- yardline_100: Nominal. Number of yards away from the goalline that the posteam is. 
- half_seconds_remaining: Nominal. Number of seconds left remaining in the half
- game_seconds_remaining: Nominal. Number of seconds left remaining in the game. 
- game_half: Categorical. Indicates whether the game is in the first or second half
- drive: Nominal. The current drive number for the game. Potentially not including in model
- sp: Categorical. Binary indicator for whether a score occurred on the play. Probably not including in model  
- down: Categorical. Indicator 1-4 of the down at the beginning of the play  
- goal_to_go: Categorical. Binary indicator showing whether or not the posteam is in a goal to go scenario
- ydstogo: Nominal. Number of yards left until the posteam achieves a first down. 
- yards_gained: Nominal. Number of yards gained on the play.   
- shotgun: Categorical. Binary indicator for whether the posteam was in the shotgun formation  
- no_huddle: Categorical. Binary indicator for whether the posteam did not huddle before the play
- qb_dropback: Categorical. Binary indicator for whether the QB dropped back on the play (pass attempt, sack, or scrambled)  
- qb_scramble: Categorical. Binary indicator for whether the QB scrambled on the play
- run_location: Categorical. The direction which the ball carrier went on a rush (Left, Middle, Right)  
- posteam_timeouts_remaining: Nominal. Number of timeouts remaining for the posteam
- defteam_timeouts_remaining: Nominal. Number of timeouts remaining for the defteam  
- posteam_score: Nominal. Number of points which the posteam has before the start of the play.   
- defteam_score: Nominal. Number of points which the defteam has before the start of the play.
- score_differential: Nominal. Difference between the posteam_score and the defteam_score. Not planning on including in model (giving model same data twice)
- epa: Nominal. Expected number of points added by the posteam on the given play. Not planning on including in model
- wp: Nominal. Winning percentage chance for the posteam on the given play. 
- penalty: Categorical. Binary indicator for whether a penalty occurred on this play  
- passer_player_name: Categorical. String to show which player threw a pass on a given play if a pass was thrown  
- passing_yards: Nominal. Number of yards the passer threw for on this play, if a pass was thrown
- receiver_player_name: Categorical. String to show which player caught a pass on a given play if a pass was thrown
- receiving_yards: Nominal. Number of yards the receiver had on this play, if a pass was thrown
- rusher_player_name: Categorical. String to show which player ran the ball on this play, if the play was a run play
- rushing_yards: Nominal. Number of yards the rusher had on this play, if the play was a run  
- penalty_team: Categorical. String abbreviation of the team that committed a penalty
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

### Data Transformations Performed
- For the Coach data (`home_coach`, `away_coach`), those columns were translated to be based upon the team who currently has possession. Therefore, the columns were reformatted to be `posteam_coach` and `defteam_coach`
- For the Quarterback data (`passer_player_name`), that column was split by game and team, and then forward and back filled. This allowed us to have a record of what quarterback was on the field on each play, and not just the quarterback who through the ball in case of a pass. This column was saved as `quarterback_on_field`

### One Hot Encoding Columns
- season_type
- posteam
- posteam_type
- defteam
- game_half
- location
- roof
- surface
- wind
- temp
- posteam_coach
- defteam_coach
- quarterback_on_field

### Convert to Boolean
- season_type
- location
- posteam_type

### Drop Time (not passed into model)
- home_team
- away_team
- yards_gained
- qb_scramble
- qb_dropback
- penalty
- passing_yards
- receiving_yards
- receiver_player_name
- rushing_yards
- rusher_player_name
- penalty_team
- weather

### Footnotes
[^1]: [Description of the NFL Play Data fields](https://www.nflfastr.com/articles/field_descriptions.html)
