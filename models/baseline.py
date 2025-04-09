import shared_methods
from sklearn.metrics import confusion_matrix


def play_type_prediction_baseline():
    df = shared_methods.return_clean_data_df()

    # make prediction using baseline model

    # baseline model:
    #   if down = 1:    run
    #   if down = 2:    pass
    #   if down = 3:    pass
    #   if down = 4 and yardline_100 > 30:     punt
    #   if down = 4 and yardline_100 <= 30:    field_goal

    down_to_play = {1: 'run', 2: 'pass', 3: 'pass', 4: 'punt'}
    df['play_prediction'] = df['down'].map(down_to_play)
    df.loc[(df['down'] == 4) & (df['yardline_100'] <= 30), 'play_prediction'] = 'field_goal'
    num_correct_df = df.loc[df['play_prediction'] == df['play_type']]
    accuracy = len(num_correct_df) / len(df)
    print(f'Baseline Accuracy: {accuracy}\n')
    print('Confusion Matrix:')
    print(confusion_matrix(df['play_type'], df['play_prediction'], labels=['run', 'pass', 'punt', 'field_goal', 'qb_kneel']))


if __name__ == '__main__':
    play_type_prediction_baseline()
