import math

def sin(num):
    '''
    Computes the sine of num (in radians).
    '''
    # Check if the input is a number (int or float).
    if (not isinstance(num, (int, float))):
        raise TypeError("Input must be a number.")

    # Check specifically if input is NaN (Not a Number)
    if (isinstance(num, float) and (num != num)):
        raise TypeError("Input must be a number.")

    # Calculate sine
    result = math.sin(num)
    if ((isinstance(num, float))):
        result = round(result, 2)

    return result

def cosine(num):
    '''
    Computes the cosine of num (in radians).
    '''
    # Check if the input is a number (int or float).
    if (not isinstance(num, (int, float))):
        raise TypeError("Input must be a number.")

    # Check specifically if input is NaN (Not a Number)
    if (isinstance(num, float) and (num != num)):
        raise TypeError("Input must be a number.")

    # Calculate cosine
    result = math.cos(num)
    if ((isinstance(num, float))):
        result = round(result, 2)

    return result

def tangent(num):
    '''
    Computes the tangent of num (in radians).
    '''
    # Check if the input is a number (int or float).
    if (not isinstance(num, (int, float))):
        raise TypeError("Input must be a number.")

    # Check specifically if input is NaN (Not a Number)
    if (isinstance(num, float) and (num != num)):
        raise TypeError("Input must be a number.")

    # Handle cases where tangent is undefined (cosine of num is 0)
    if (cosine(num) == 0):
        raise ValueError(f"Tangent is undefined at {num}")

    # Calculate tangent
    result = math.tan(num)
    if ((isinstance(num, float))):
        result = round(result, 2)

    return result

