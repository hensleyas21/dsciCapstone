import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from argparse import ArgumentParser


def train_model(model_type):
    # read in initial data and drop columns not included in the model
    # Note: this is specifically for the model related to predicting play_type.
    cols_to_keep = ['play_type', 'home_team', 'away_team', 'season_type', 'week', 'posteam', 'posteam_type', 'defteam',
                    'yardline_100',
                    'half_seconds_remaining', 'game_seconds_remaining', 'game_half', 'drive', 'qtr', 'down',
                    'goal_to_go', 'ydstogo', 'shotgun',
                    'no_huddle', 'posteam_timeouts_remaining', 'defteam_timeouts_remaining', 'posteam_score',
                    'defteam_score', 'score_differential',
                    'epa', 'wp', 'season', 'start_time', 'stadium', 'location', 'div_game', 'roof', 'surface', 'temp',
                    'wind',
                    'home_coach', 'away_coach']
    df = pd.read_csv('../cleaned_data.csv')
    df = df.loc[:, cols_to_keep]

    print(f'columns before encoding = {list(df.columns)}')

    one_hot_encoding_fields = ['home_team', 'away_team', 'season_type', 'posteam', 'drive',
                               'posteam_type', 'defteam', 'game_half', 'start_time', 'stadium', 'location', 'roof',
                               'surface',
                               'temp', 'wind', 'home_coach', 'away_coach']

    df = pd.get_dummies(df, columns=one_hot_encoding_fields)
    print(f'num cols = {len(df.columns)}')

    play_type_to_num = {'pass': 0, 'run': 1, 'punt': 2, 'field_goal': 3, 'qb_kneel': 4, 'qb_spike': 5}
    df['play_type'] = df['play_type'].map(play_type_to_num)

    print('Splitting into test and train')
    df = df.sample(n=50000)
    X = df.drop(columns=['play_type'])
    y = df['play_type']
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    print(f'Train Length = {len(X_train)}')
    print(f'Test Length = {len(X_test)}')

    print('Training Model')
    model_type.fit(X_train, y_train)

    print('Predicting Model')
    y_pred = model_type.predict(X_test)
    acc: float = float(accuracy_score(y_test, y_pred))
    print(f'Accuracy: {acc * 100:.2f}%')


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-m', '--model', type=str,
                        help='Name of the model to be used. Valid Options: [DecisionTreeClassifier, GaussianNB, KNeighborsClassifier, LogisticRegression, RandomForestClassifier, LinearSVC]')
    args = parser.parse_args()
    model = None

    try:
        if args.model == 'DecisionTreeClassifier':
            model = DecisionTreeClassifier()
        elif args.model == 'GaussianNB':
            model = GaussianNB()
        elif args.model == 'KNeighborsClassifier':
            model = KNeighborsClassifier()
        elif args.model == 'LogisticRegression':
            model = LogisticRegression()
        elif args.model == 'RandomForestClassifier':
            model = RandomForestClassifier()
        elif args.model == 'LinearSVC':
            model = LinearSVC()
        else:
            raise ValueError('Model type not recognized. Please input one in the following list:\n'
                             '[DecisionTreeClassifier, GaussianNB, KNeighborsClassifier, LogisticRegression, RandomForestClassifier, LinearSVC]')
        train_model(model)
    except ValueError as e:
        print(e)
