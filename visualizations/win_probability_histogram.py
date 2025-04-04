import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def output_win_probability_histogram():
    # Output a stacked bar histogram, where each bin is a 5% window of a team's chance to win the game
    df = pd.read_csv('../cleaned_data.csv')

    df['play_type'] = df['play_type'][df['play_type'].isin(['run', 'pass'])]
    df = df[['play_type', 'wp']]

    bins = np.linspace(0, 1, 21)
    df['wp_bin'] = pd.cut(df['wp'], bins)

    # Group by team, get count of pass and run
    df = df.groupby(['wp_bin']).agg(
        run_count=('play_type', lambda x: (x == 'run').sum()),
        pass_count=('play_type', lambda x: (x == 'pass').sum()),
        total=('play_type', lambda x: (x.isin(['run', 'pass'])).sum()),
    ).reset_index()

    df['run_ratio'] = df['run_count'] / df['total']
    df['pass_ratio'] = df['pass_count'] / df['total']

    df = df[['wp_bin', 'run_ratio', 'pass_ratio']].rename(columns={'run_ratio': 'Run', 'pass_ratio': 'Pass'})

    df.plot(kind='bar', stacked=True, width=1)
    plt.title('Run/Pass Ratio by Win Probability')
    plt.xlabel('Win Probability ')
    plt.ylabel('Percentage Ratio')
    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False
    )
    plt.yticks(ticks=bins)
    plt.savefig('charts/win_probability_histogram.png')


if __name__ == '__main__':
    output_win_probability_histogram()
