from sklearn.feature_selection import SelectKBest, f_classif
from shared_methods import return_clean_data_df

df_all_rows = return_clean_data_df()

df = df_all_rows.sample(100000)

prediction_col = 'play_type'

X, y = df.drop(columns=[prediction_col]), df[[prediction_col]]

X_new = SelectKBest(f_classif, k=20).fit(X, y)
print(X_new.get_feature_names_out())