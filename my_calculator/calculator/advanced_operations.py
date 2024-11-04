import sys
import math

def power(base, exponent):
    '''
    Raises base to exponent power.
    '''
    result = 0

    # Checks if both numbers are either int or float.
    if not ((isinstance(base, (int, float)) and isinstance(exponent, (int, float)))):
        raise TypeError("Both inputs must be numbers.")
   
    # Checks specifically if either inputs are Nan (Not a Number)
    if ((isinstance(base, float) and (base != base)) or (isinstance(exponent, float) and (exponent != exponent))):
        raise TypeError("Both inputs must be numbers.")

    # Some zero base cases
    if (base == 0):
        if (exponent == 0):
            raise ValueError("0 to the 0 power is undefined.")

        if (exponent < 0):
            raise ZeroDivisionError('Zero cannot be raised to a negative exponent.')
    
        if (exponent == float('inf')):
            return 0.0

        if (exponent == float('-inf')):
            raise ZeroDivisionError('Zero to the negative infinity is undefined.')
    
    # Weird Infinity cases
    if ((base == float('inf') or base == float('-inf')) or (exponent == float('inf') or exponent == float('-inf'))):
        if ((base is not float('inf') and base > 0) and exponent == float('inf')):
            return float('inf')

        if ((base is not float('inf') and base > 0) and exponent == float('-inf')):
            return 0.0

        if (base == float('inf') and exponent == float('inf')):
            return float('inf')

        if (base == float('-inf') and exponent == float('inf')):
            raise ValueError('Negative infinity to positive infinity is undefined.')

        if (base == float('-inf') and (exponent < 0 and not (exponent.is_integer()))):
            raise ValueError('Negative infinity raised to fractional exponents is undefined.')

        if (base == float('-inf') and (exponent > 0 and exponent.is_integer())):
            if (exponent > 0):
                return float('-inf')

            if (exponent < 0):
                return 0.0
            
            if (exponent == 0):
                return 1.0

    result = base ** exponent

    # Check if either input number is a float. If so, perform the addition and round off to 2 digits.
    if ((isinstance(base, float)) or (isinstance(exponent, float))):
        result = round(result, 2)

    # Check for integer/float overflow and underflow.
    if (isinstance(result, int) and (result > sys.maxsize or result < (-sys.maxsize - 1))):
        raise OverflowError("Integer overflow/underflow")
    elif (isinstance(result, float) and (result > sys.float_info.max or result < sys.float_info.min)):
        raise OverflowError("Float overflow/underflow")

    return result

def square_root(num):
    '''
    Computes the square root of the given num.
    '''
    # Check if the input is a number (int or float).
    # Checks if both numbers are either int or float.
    if not ((isinstance(num, (int, float)))):
        raise TypeError("Both inputs must be numbers.")
   
    # Checks specifically if either inputs are Nan (Not a Number)
    if ((isinstance(num, float)) and (num != num)):
        raise TypeError("Both inputs must be numbers.")

    # Handle edge case for zero
    if (num == 0):
        return 0.0

    # Handle edge case for negative numbers
    if (num < 0):
        raise ValueError("Cannot compute the square root of a negative number.")

    # Handle edge case for positive infinity
    if (num == float('inf')):
        return float('inf')
    elif (num == float('-inf')):
        raise ValueError("Cannot compute the square root of negative infinity")

    # Handle edge case for positive nums
    result = math.sqrt(num)
    result = round(result, 2)

    # Check for integer/float overflow and underflow.
    if (isinstance(result, int) and (result > sys.maxsize)):
        raise OverflowError("Integer overflow/underflow")
    elif (isinstance(result, float) and (result > sys.float_info.max)):
        raise OverflowError("Float overflow/underflow")

    return result

def factorial(n):
    '''
    Computes the factorial of a non-negative integer n.
    '''
    # Check if the input is an integer.
    if (not isinstance(n, int)):
        raise TypeError("Input must be a non-negative integer.")
    
    # Handle negative inputs
    if (n < 0):
        raise ValueError("Factorial is not defined for negative numbers.")

    # Handle the factorial of 0
    if (n == 0):
        return 1

    # Initialize the result
    result = 1

    # Calculate factorial iteratively
    for i in range(1, n + 1):
        result *= i
        
        # Check for integer overflow
        if (result > sys.maxsize):
            raise OverflowError("Integer overflow/underflow")

    return result
