from sklearn.feature_selection import SelectKBest, f_classif

def return_feature_selection_rows(df):
    df = df.sample(300000)

    prediction_col = 'play_type'

    X, y = df.drop(columns=[prediction_col]), df[[prediction_col]]

    X_new = SelectKBest(f_classif, k=20).fit(X, y)
    rows = X_new.get_feature_names_out()
    return rows
