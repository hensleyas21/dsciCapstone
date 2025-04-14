import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def output_win_probability_histogram():
    # Output a stacked bar histogram, where each bin is a 5% window of a team's chance to win the game
    df = pd.read_csv('../cleaned_data.csv')

    # Filter only 'run' and 'pass' play types
    df['play_type'] = df['play_type'][df['play_type'].isin(['run', 'pass'])]
    df = df[['play_type', 'wp']]

    bins = np.linspace(0, 1, 21)
    df['wp_bin'] = pd.cut(df['wp'], bins)

    # Group by wp, get count of pass and run
    df = df.groupby(['wp_bin']).agg(
        run_count=('play_type', lambda x: (x == 'run').sum()),
        pass_count=('play_type', lambda x: (x == 'pass').sum()),
        total=('play_type', lambda x: (x.isin(['run', 'pass'])).sum()),
    ).reset_index()

    # Calculate ratios
    df['run_ratio'] = df['run_count'] / df['total']
    df['pass_ratio'] = df['pass_count'] / df['total']

    # Prepare the data for plotting
    df = df[['wp_bin', 'run_ratio', 'pass_ratio']].rename(columns={'run_ratio': 'Run', 'pass_ratio': 'Pass'})

    # Create a bar plot (stacked)
    df.set_index('wp_bin')[['Run', 'Pass']].plot(kind='bar', stacked=True, width=1, color=['#a3221d', '#5799c7'], alpha=1.0, figsize=(10,7))

    # Add labels and title
    plt.title('Run/Pass Ratio by Win Probability', fontsize=24)
    plt.xlabel('Win Probability', fontsize=16)
    x_tick_labels = np.arange(0, 1.01, .1)
    x_tick_labels = [f"{x:.1f}" for x in x_tick_labels]
    tick_positions = np.arange(0, 21, 2) - 0.5  # shift 0.5 left
    plt.xticks(ticks=tick_positions, labels=x_tick_labels, fontsize=12)
    plt.ylabel('Percentage Ratio', fontsize=16)
    plt.yticks(ticks=np.arange(0, 1.01, .1), fontsize=12)

    # Customize legend
    plt.legend(fontsize=12, title_fontsize=16)
    plt.tight_layout()
    plt.savefig('charts/win_probability_histogram.svg')
    plt.show()


if __name__ == '__main__':
    output_win_probability_histogram()
