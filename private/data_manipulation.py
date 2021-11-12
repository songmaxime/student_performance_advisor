import pandas as pd
import yaml


def load_student_profile(filename):
    """Read and load data from a csv file and separate the data into X and y

    args:
        filename (str): name of the csv file

    returns:
        X (pandas.DataFrame): contains all the information students that will be used to do a profiling
        y (pandas.DataFrame): correspond to the variable G3 which indicate the final grade of each student
    """
    data = pd.read_csv(filename, sep=';', header='infer')
    y = data['G3']
    # we keep G2 and assume that this variable indicates the current level of the student
    # meanwhile G1 is highly correlated to G2 and we can safely remove this variable
    X = data.drop(['G3', 'G1'], 1)

    return X, y


def get_background_variables(X):
    """Get the dataset with only the background variables.

    Args:
        X (pandas.DataFrame): DataFrame loaded from data/student-mat.csv or data/student-por.csv

    Returns:
        X_background (pandas.DataFrame): X with all non-related-background variables removed
    """
    background_column_names = ["school","sex","age","address","famsize","Pstatus","Medu","Fedu",\
                               "Mjob","Fjob","reason","guardian","traveltime","failures","nursery","G2"]
    X_background = X[background_column_names]
    return X_background


def get_predictor_variables(X):
    """Get the dataset with only the variables used for advices

    Args:
        X (pandas.DataFrame): DataFrame loaded from data/student-mat.csv or data/student-por.csv

    Returns:
        X_predictor (pandas.DataFrame): X with all non-related-background variables removed
    """
    predictor_column_names = ["studytime","schoolsup","famsup","paid","activities","higher","internet",\
                              "romantic","famrel","freetime","goout","Dalc","Walc","health","absences"]
    X_predictor = X[predictor_column_names]
    return X_predictor


def load_current_student_profile_from_yaml(filename):
    """Loads a yaml file containing the information from a student and returns the information in a pandas.DataFrame
    """
    with open(filename) as file:
        # The FullLoader parameter handles the conversion from YAML
        info = yaml.load(file, Loader=yaml.FullLoader)
    # to transform a dict to a dataframe, the value of each key in the dict should be an array
    # the length of the array being the number of rows in the dataframe
    for key in info:
        # yes and no are automatically converted to boolean, so we have to convert it back to str "yes" or "no"
        if type(info[key]) == bool:
            info[key] = ["yes" if info[key] else "no"]
        else:
            info[key] = [info[key]]
    return pd.DataFrame.from_dict(info)


def categorical_to_numeric(data):
    """Transform all categorical variables in a DataFrame to numerical variables using OneHotEncoder
    """
    categorical_columns_name = []
    for name in data.columns:
        if data[name].dtype == 'object':
            categorical_columns_name.append(name)
    # drop the first category of each categorical variable
    return pd.get_dummies(data, columns=categorical_columns_name, drop_first=True)