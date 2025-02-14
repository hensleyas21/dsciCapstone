import pandas as pd
from data_cleaning.data_inspector import make_plot, make_boxplot, make_barplot

def main():
    df = pd.read_csv('../data/play_by_play_2024.csv')
    make_barplot(df['play_type']).show()


if __name__ == '__main__':
    main()
