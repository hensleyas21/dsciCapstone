import pandas as pd
import matplotlib.pyplot as plt

SEASON = 2020

def output_stacked_bar_chart():
    df = pd.read_csv('../cleaned_data.csv')

    # Stacked Bar Chart: Show each team on the X-axis, Play type (just run and pass) on the Y-axis. Just for certain seasons

    # Exclude all values that do not match the current season
    df = df[df['season'] == SEASON]

    # Exclude all values that aren't run or pass in play_type
    df['play_type'] = df['play_type'][df['play_type'].isin(['run', 'pass'])]
    df = df[['play_type', 'posteam']]

    # Group by team, get count of pass and run
    df = df.groupby(['posteam']).agg(
        run_count=('play_type', lambda x: (x == 'run').sum()),
        pass_count=('play_type', lambda x: (x == 'pass').sum()),
        total=('play_type', lambda x: (x.isin(['run', 'pass'])).sum()),
    ).reset_index()

    df['run_ratio'] = df['run_count'] / df['total']
    df['pass_ratio'] = df['pass_count'] / df['total']

    df = df[['posteam', 'run_ratio', 'pass_ratio']]

    df = df.sort_values(by='run_ratio', ascending=False)

    df = df.set_index('posteam').rename(columns={'run_ratio': 'Run', 'pass_ratio': 'Pass'})
    df.plot(kind='bar', stacked=True)
    plt.title(f'Run/Pass Ratio by Team in {SEASON}')
    plt.legend(loc='upper left')
    plt.xlabel("Offensive Team")
    plt.ylabel("Percentage")
    plt.savefig('charts/stacked_bar_chart.png')


if __name__ == '__main__':
    output_stacked_bar_chart()
