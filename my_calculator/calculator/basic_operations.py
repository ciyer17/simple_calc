import sys

def add(num1, num2):
    '''
    Performs addition of two numbers.
    '''
    result = 0

    # Checks if both numbers are either int or float.
    if not ((isinstance(num1, (int, float)) and isinstance(num2, (int, float)))):
        raise TypeError("Both inputs must be numbers.")
   
    # Checks specifically if either inputs are Nan (Not a Number)
    if ((isinstance(num1, float) and (num1 != num1)) or (isinstance(num2, float) and (num2 != num2))):
        raise TypeError("Both inputs must be numbers.")

    # Infinity checks
    if (num1 == float('inf') or num2 == float('inf')):
        return float('inf')
    elif (num1 == float('-inf') or num2 == float('-inf')):
        return float('-inf')

    result = num1 + num2
    # Check if either input number is a float. If so, perform the addition and round off to 2 digits.
    if ((isinstance(num1, float)) or (isinstance(num2, float))):
        result = round(result, 2)

    # Check for integer/float overflow and underflow.
    if (isinstance(result, int) and (result > sys.maxsize or result < (-sys.maxsize - 1))):
        raise OverflowError("Integer overflow/underflow")

    return result

def subtract(num1, num2):
    '''
    Performs subtraction of two numbers.
    '''
    result = 0

    # Checks if both numbers are either int or float.
    if not ((isinstance(num1, (int, float)) and isinstance(num2, (int, float)))):
        raise TypeError("Both inputs must be numbers.")
   
    # Checks specifically if either inputs are Nan (Not a Number)
    if ((isinstance(num1, float) and (num1 != num1)) or (isinstance(num2, float) and (num2 != num2))):
        raise TypeError("Both inputs must be numbers.")
    
    # Infinity checks
    if (num1 == float('inf') or num2 == float('inf')):
        return float('inf')
    elif (num1 == float('-inf') or num2 == float('-inf')):
        return float('-inf')

    result = num1 - num2
    # Check if either input number is a float. If so, perform the addition and round off to 2 digits.
    if ((isinstance(num1, float)) or (isinstance(num2, float))):
        result = round(result, 2)

    # Check for integer/float overflow and underflow.
    if (isinstance(result, int) and (result > sys.maxsize or result < (-sys.maxsize - 1))):
        raise OverflowError("Integer overflow/underflow")

    return result

def multiply(num1, num2):
    '''
    Performs multiplication of two numbers.
    '''
    result = 0

    # Checks if both numbers are either int or float.
    if not ((isinstance(num1, (int, float)) and isinstance(num2, (int, float)))):
        raise TypeError("Both inputs must be numbers.")
   
    # Checks specifically if either inputs are Nan (Not a Number)
    if ((isinstance(num1, float) and (num1 != num1)) or (isinstance(num2, float) and (num2 != num2))):
        raise TypeError("Both inputs must be numbers.")

    # Handle infinity cases
    if (num1 == float('inf') or num2 == float('inf')):
        if (num1 == 0 or num2 == 0):
            return float('nan')  # 0 * inf is undefined
        if ((num1 > 0 or num2 > 0) or (num1 < 0 or num2 < 0)):
            return float('inf')
        else:
            return float('-inf')
    elif (num1 == float('-inf') or num2 == float('-inf')):
        if (num1 == 0 or num2 == 0):
            return float('nan')  # 0 * -inf is undefined
        if ((num1 > 0 or num2 < 0) or (num1 < 0 or num2 > 0)):
            return float('-inf')
        else:
            return float('inf')

    result = num1 * num2
    # Check if either input number is a float. If so, perform the addition and round off to 2 digits.
    if ((isinstance(num1, float)) or (isinstance(num2, float))):
        result = round(result, 2)

    # Check for integer/float overflow and underflow.
    if (isinstance(result, int) and (result > sys.maxsize or result < (-sys.maxsize - 1))):
        raise OverflowError("Integer overflow/underflow")

    return result

def divide(dividend, divisor):
    '''
    Performs division of two numbers.
    '''
    result = 0

    # Checks if both numbers are either int or float.
    if not ((isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)))):
        raise TypeError("Both inputs must be numbers.")
   
    # Checks specifically if either inputs are Nan (Not a Number)
    if ((isinstance(dividend, float) and (dividend != dividend)) or (isinstance(divisor, float) and (divisor != divisor))):
        raise TypeError("Both inputs must be numbers.")

    if (divisor == 0):
        raise ZeroDivisionError('Divisor cannot be zero')

    # Handle infinity cases
    if (dividend == float('inf') or dividend == float('-inf')):
        if (divisor == float('inf') or divisor == float('-inf')):
            return float('nan')
        else:
            return float('-inf')
    elif (divisor == float('inf') or divisor == float('-inf')):
        return 0.0

    result = dividend / divisor

    # Check if either input number is a float. If so, perform the addition and round off to 2 digits.
    if ((isinstance(dividend, float)) or (isinstance(divisor, float))):
        result = round(result, 2)

    # Check for integer/float overflow and underflow.
    if (isinstance(result, int) and (result > sys.maxsize or result < (-sys.maxsize - 1))):
        raise OverflowError("Integer overflow/underflow")

    return result
