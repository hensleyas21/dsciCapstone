import pandas as pd

df = pd.read_csv('data/cleaned_data.csv')

df.sample(frac=.01).to_csv('random_sample.csv')

print(df.columns)