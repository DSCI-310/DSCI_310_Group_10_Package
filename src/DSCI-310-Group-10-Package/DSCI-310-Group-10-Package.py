"""
    A function used to format a pandas generic histograms

    Parameters
    ----------
    alpha: List of integer
            A list of Hyperparameter used to tune Ridge
    processor: chaining of sklearn estimators
                Estimators used to transform a given dataset
    trainx: pandas DataFrame
                A dataframe that contains the training set for Ridge
    trainy: pandas Series
                A Series of classifications for a given observation
    cv: An integer
            Integer represent the number of cross validation
    Raises
    ------
    TypeError:
        if the alpha is not the correct type
        if the cv is not the correct type
        if the trainx is not the correct type
        if the trainy is not the correct type
    """
from alpha_tuning.py import ridge_alpha_tuning

'''
    A function used to format a pandas generic histograms
    
    Parameters
    ----------
    df : Pandas DataFrame
        Dataframe with n features to map.
    texts : dictionary
        A dictionary with labels for each histogram. Should
        consist of xaxes, titles, and yaxes.
    fontsize : int
        fontsize of the histograms
    
    Raises
    ------
    ValueError:
        if the texts parameter is empty.
    '''
from format_histograms.py import format_histograms

