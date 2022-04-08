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

 """
    The function inv_outcome_plot generates a normalized stacked bar charts showing proportions of 
    major earner/non major earner individuals that made money on investments 
    and proportion of individuals that lost money on investments among families 
    of different size
    
    Parameters
    ----------
    grouped_df : Pandas DataFrame
        Dataframe grouped by size.
    size_col : String
        name of column of integers corresponding to family sizes
    bar_split_col : String
        name of column of binary integers corresponding to variable stacked bar chart is split on
    val_col : String
        name of column of boolean corresponding to results of investments given in boolean
        NOTE: this can be the predicted values from model, or actual values from data
    counts_col : String
        name of column of integers corresponding to counts of each group
    major_earner : Boolean
        True indicates plots portray investment income outcome data for major income earners, 
        False indicates plots portray investment income outcome for non major income earners
    fig_title : String
        name of figure
    fig_ylabel : String
        name of y axis of stacked bar chart plot
    
    
    Raises
    ------
    TypeError:
        if grouped_df is not a DataFrame
        if size_col is not a String
        if grouped_df[size_col] is not a column of integers
        if bar_split_col is not a String
        if grouped_df[bar_split_col] is not a columns of binary integers (2 integers)
        if val_col is not a String
        if grouped_df[val_col] is not a column of boolean
        if counts_col is not a String
        if grouped_df[counts_col] is not a column of integers
        if major_earner is not a Boolean
        if fig_title is not a String
        if fig_ylabel is not a String
    """
from inv_outcome_plot.py import inv_outcome_plot

"""
    A function used to format a pandas generic histograms

    Parameters
    ----------
    processor: chaining of sklearn estimators
                Estimators used to transform a given dataset
    trainx: pandas DataFrame
                A dataframe that contains the training set for Ridge
    trainy: pandas Series
                A Series of classifications for a given observation
    param_grid: an list
        Series of K values to allow for hyperparameter tuning
    Raises
    ------
    TypeError:
        if the trainx is not the correct type
        if the trainy is not the correct type
    """
from KNN_tuning.py import KNN_tuning

"""
    Splits the given dataset into a training set and a testing set, 
    further splitting each set into one without a specified column,
    and one with only said specified column.
    
    Parameters
    ----------
    data : Pandas DataFrame
        Dataframe to split into training and testing
    test_size : Double, value between 0 and 1
        The percentage of the input dataframe that will be used to make the testing set 
    rn : int
       A random number to make the split reprodicable
    col : String
       quoted column name of column to be dropped from 2 testing datasets and 2 testing datasets
    
    Raises
    ------
    TypeError:
        if the dataframe is not of the correct type
        if the random number is not a number
        if column name is not a string
        
    ValueError:
        if the test_size is not a number between 0-1
        if specified column is not in the dataset
        if dataset has less than 10 observations
    """
from split_drop.py import split_drop