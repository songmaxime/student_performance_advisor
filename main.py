import pandas as pd

import private.data_manipulation as data
import private.kmeans as kmeans
import private.random_forest as rf


def main(filename):

    # this is the student we wish to give advice
    student_info = data.load_current_student_profile_from_yaml("data/student.yaml")

    # pandas.DataFrame
    X, y = data.load_student_profile(filename)

    # add the current student profile to the existing dataset
    X_augmented = X.append(student_info, ignore_index=True)

    # split X into X_background and X_predictor
    X_background = data.get_background_variables(X_augmented)
    X_predictor = data.get_predictor_variables(X)

    # One-Hot encoding of nominal variables
    X_background_numeric = data.categorical_to_numeric(X_background)
    X_predictor_numeric = data.categorical_to_numeric(X_predictor)

    X_background_array = X_background_numeric.to_numpy()
    labels = kmeans.trained_kmeans(X_background_array)

    # get all students that are in the same cluster as student_info
    X_predictor_cluster, y_cluster = kmeans.get_X_y_clusters(X_predictor_numeric, y, labels[:-1], labels[-1])

    X_predictor_array = X_predictor_cluster.to_numpy()
    y_array = y_cluster.to_numpy()

    # get feature importances and decide which action to put in priority
    print(pd.DataFrame([rf.get_feature_importances(X_predictor_array, y_array)], columns=X_predictor_cluster.columns).iloc[0].sort_values(ascending=False))

if __name__ == '__main__':
    main("data/student-mat.csv")
