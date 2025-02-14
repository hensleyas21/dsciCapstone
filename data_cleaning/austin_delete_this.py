import pandas as pd

from data_inspector import make_plot, make_density_plot, make_boxplot

if __name__ == '__main__':
    data = [1, 2, 3, 4, 1, 2, 3, 3, 3, 4, 5, 2, 2, 2]
    make_boxplot(data).show()