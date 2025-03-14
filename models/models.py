from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from argparse import ArgumentParser
import pickle
import shared_methods

def train_model(model_type):
    df = shared_methods.return_clean_data_df()
    play_type_to_num = {'pass': 0, 'run': 1, 'punt': 2, 'field_goal': 3, 'qb_kneel': 4, 'qb_spike': 5}
    df['play_type'] = df['play_type'].map(play_type_to_num)
    print('Splitting into test and train')

    # NOTE FOR DR. DICKINSON: Whenever the model was run with 300,000 records or more, the results took an extraordinary amount of time to run
    # Additionally, past a certain point the model would refuse to run the `fit()` method at all if the dataset was too large (500,000+ records)
    # We sampled 100,000 records for the initial models, and plan to talk to you about the best way to chunk the dataset for future models.

    df = df.sample(n=100000)
    X = df.drop(columns=['play_type'])
    y = df['play_type']
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    print(f'Train Length = {len(X_train)}')
    print(f'Test Length = {len(X_test)}')

    print('Training Model')
    model_type.fit(X_train, y_train)

    print('Predicting Model')
    y_pred = model_type.predict(X_test)
    acc: float = float(accuracy_score(y_test, y_pred))
    print(f'Accuracy: {acc * 100:.2f}%')

    print('saving model to file')
    filename = 'model.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(model_type, file)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-m', '--model', type=str,
                        help='Name of the model to be used. Valid Options: [DecisionTreeClassifier, GaussianNB, KNeighborsClassifier, LogisticRegression, RandomForestClassifier, LinearSVC]')
    args = parser.parse_args()
    model = None

    try:
        if args.model == 'DecisionTreeClassifier':
            model = DecisionTreeClassifier()
        elif args.model == 'GaussianNB':
            model = GaussianNB()
        elif args.model == 'KNeighborsClassifier':
            model = KNeighborsClassifier()
        elif args.model == 'LogisticRegression':
            model = LogisticRegression()
        elif args.model == 'RandomForestClassifier':
            model = RandomForestClassifier()
        elif args.model == 'LinearSVC':
            model = LinearSVC()
        else:
            raise ValueError('Model type not recognized. Please input one in the following list:\n'
                             '[DecisionTreeClassifier, GaussianNB, KNeighborsClassifier, LogisticRegression, RandomForestClassifier, LinearSVC]')
        train_model(model)
    except ValueError as e:
        print(e)
