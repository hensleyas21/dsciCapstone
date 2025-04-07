import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def output_win_probability_histogram():
    # Output a stacked bar histogram, where each bin is a 5% window of a team's chance to win the game
    df = pd.read_csv('../cleaned_data.csv')

    df['play_type'] = df['play_type'][df['play_type'].isin(['run', 'pass'])]
    df = df[['play_type', 'wp']]

    df['run_ratio'] = df['run_count'] / df['total']
    df['pass_ratio'] = df['pass_count'] / df['total']

    df = df.groupby(['wp']).agg(
        run_count=('play_type', lambda x: (x == 'run').sum()),
        pass_count=('play_type', lambda x: (x == 'pass').sum()))

    df = df.rename(columns={'run_ratio': 'Run', 'pass_ratio': 'Pass'})

    sns.histplot(data=df, x='wp')
    plt.title('Run/Pass Ratio by Win Probability')
    plt.xlabel('Win Probability')
    plt.xticks(ticks=np.arange(0, 1.01, .05))
    plt.ylabel('Percentage Ratio')
    plt.yticks(ticks=np.arange(0, 1.01, .1))
    plt.savefig('charts/win_probability_histogram.svg')
    plt.show()


if __name__ == '__main__':
    output_win_probability_histogram()
