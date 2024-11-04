import math
import sys

def logarithm(num, base):
    '''
    Computes the logarithm of num with the specified base.
    '''
    # Checks if both numbers are either int or float.
    if not ((isinstance(num, (int, float)) and isinstance(base, (int, float)))):
        raise TypeError("Both inputs must be numbers.")
   
    # Checks specifically if either inputs are Nan (Not a Number)
    if ((isinstance(num, float) and (num != num)) or (isinstance(base, float) and (base != base))):
        raise TypeError("Both inputs must be numbers.")

    # Handle negative and zero values for logarithm
    if (num <= 0):
        raise ValueError("Logarithm is undefined for zero or negative values.")
    if (base <= 0):
        raise ValueError("Base cannot be negative.")

    # Handle infinity input for logarithm
    if (num == float('inf')):
        return float('inf')

    if (num == float('-inf')):
        raise ValueError("Logarithm for negative infinity is undefined.")

    # Calculate logarithm
    result = math.log(num, base)
    result = round(result, 2)

    # Check for integer/float overflow and underflow.
    if (isinstance(result, int) and (result > sys.maxsize or result < (-sys.maxsize - 1))):
        raise OverflowError("Integer overflow/underflow in logarithm.")

    return result

def natural_log(num):
    '''
    Computes the natural logarithm of num. Base is always the mathematical constant e.
    '''
    return logarithm(num, math.e)

def exponential(num):
    '''
    Computes the exponential of num (e^num).
    '''
    # Check if the input is a number (int or float).
    if (not isinstance(num, (int, float))):
        raise TypeError("Input must be a number.")

    # Check specifically if input is NaN (Not a Number)
    if (isinstance(num, float) and (num != num)):
        raise TypeError("Input must be a number.")

    # Handle large inputs for exponential
    if (num > math.log(sys.float_info.max)):
        raise OverflowError("Enumponential overflow for large input")

    # Handle negative infinity input
    if (num == float('-inf')):
        return 0.0

    # Calculate enumponential
    result = math.exp(num)
    result = round(result, 2)

    # Check for float overflow/underflow.
    if (isinstance(result, float) and (result > sys.float_info.max or result < sys.float_info.min)):
        raise OverflowError("Float overflow/underflow in exponential calculation")

    return result
