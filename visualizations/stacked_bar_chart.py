import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SEASON = 2024

def output_stacked_bar_chart():
    df = pd.read_csv('../cleaned_data.csv')

    # Filter to current season and only run/pass plays
    df = df[df['season'] == SEASON]
    df = df[df['play_type'].isin(['run', 'pass'])]

    # Keep only necessary columns
    df = df[['play_type', 'posteam']]

    # Count play types per team
    count_df = df.groupby(['posteam', 'play_type']).size().reset_index(name='count')

    # Pivot and calculate ratios
    pivot_df = count_df.pivot(index='posteam', columns='play_type', values='count').fillna(0)
    pivot_df['total'] = pivot_df['run'] + pivot_df['pass']
    pivot_df['run_ratio'] = pivot_df['run'] / pivot_df['total']
    pivot_df['pass_ratio'] = pivot_df['pass'] / pivot_df['total']
    pivot_df = pivot_df.sort_values(by='run_ratio', ascending=False).reset_index()

    # Prepare data
    teams = pivot_df['posteam']
    run_vals = pivot_df['run_ratio']
    pass_vals = pivot_df['pass_ratio']

    colors = {'Run': '#a3221d', 'Pass': '#5799c7'}

    # Plot using matplotlib for true stacked bars
    fig, ax = plt.subplots(figsize=(10, 7))
    bar_width = 1.0
    x = np.arange(len(teams))

    ax.bar(x, run_vals, width=bar_width, color=colors['Run'], label='Run')
    ax.bar(x, pass_vals, width=bar_width, bottom=run_vals, color=colors['Pass'], label='Pass')

    # Final plot formatting
    ax.set_title(f'Run/Pass Ratio by Team in {SEASON}', fontsize=24)
    ax.set_xlabel('Offensive Team', fontsize=16)
    ax.set_ylabel('Percentage', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(teams, rotation=90, fontsize=12)
    ax.set_yticks(np.arange(0, 1.01, 0.1))
    ax.tick_params(axis='y', labelsize=12)
    ax.legend(title='Play Type', fontsize=12, title_fontsize=16)

    plt.tight_layout()
    plt.savefig('charts/stacked_bar_chart.svg')
    plt.show()

if __name__ == '__main__':
    output_stacked_bar_chart()
