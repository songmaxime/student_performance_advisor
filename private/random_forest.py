from sklearn.ensemble import RandomForestRegressor

def get_feature_importances(X_advice_cluster_array, y_cluster_array):
    """Get the importance of each variables and give personalized advice

    Args:
        X_advice_cluster_array (numpy.ndarray): student profiles sharing the same background
        y_cluster_array (numpy.ndarray): final grade of students
    """
    regr = RandomForestRegressor(n_estimators=10, max_depth=4)
    regr.fit(X_advice_cluster_array, y_cluster_array)
    return regr.feature_importances_