from sklearn.cluster import KMeans


def trained_kmeans(X_background_array):
    """train kmeans on the student performance dataset and return cluster assignments
    """
    regr = KMeans(n_clusters=17, random_state=0).fit(X_background_array)
    return regr.labels_


def get_X_y_clusters(X_predictor, y, labels, cluster):
    """Get all the student profiles from the same cluster

    Args:
        X_predictor (pandas.DataFrame): dataset containing all the variables used for advices
        y : final grade of students
        labels (numpy.ndarray): cluster assignation for each student
        cluster (int): the cluster we are interest in

    Returns:
        X_predictor_cluster (pandas.DataFrame): data with all student from cluster
        y_cluster : final grade of all student from cluster
    """
    X_predictor_cluster = X_predictor.iloc[labels == cluster]
    y_cluster = y.iloc[labels == cluster]
    return X_predictor_cluster, y_cluster