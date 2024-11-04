# References:
# Mean:https://www.geeksforgeeks.org/python-statistics-mean-function/
# Median: https://www.geeksforgeeks.org/find-median-of-list-in-python/
# Mode: https://www.geeksforgeeks.org/python-statistics-mode-function/
# Standard Deviation: https://www.geeksforgeeks.org/python-statistics-stdev/

import statistics

def _validate_data(data):
    '''
    Validates that the input is a list containing only int or float values.
    '''
    # Check if data is a list
    if not (isinstance(data, list)):
        raise TypeError("Input must be a list.")

    # Check if all elements in the list are int or float
    for item in data:
        if not (isinstance(item, (int, float))):
            raise ValueError("All elements in the list must be int or float.")

    # Check list is not empty
    if (len(data) == 0):
        raise ValueError("The list must not be empty.")

def mean(data):
    '''
    Computes the mean of a list of numbers.
    '''
    _validate_data(data)
    result = statistics.mean(data)
    result = round(result, 2)
    return result

def median(data):
    '''
    Computes the median of a list of numbers.
    '''
    _validate_data(data)
    result = statistics.median(data)
    result = round(result, 2)
    return result

def mode(data):
    '''
    Computes the mode of a list of numbers.
    '''
    _validate_data(data)
    try:
        result = statistics.mode(data)
        result = round(result, 2)
        return result
    except statistics.StatisticsError:
        raise ValueError("Mode is undefined for this dataset.")

def standard_deviation(data):
    '''
    Computes the standard deviation of a list of numbers.
    '''
    if (len(data) < 2):
        raise ValueError("At least two data points are required to calculate standard deviation.")

    _validate_data(data)
    result = statistics.stdev(data)
    result = round(result, 2)
    return result

