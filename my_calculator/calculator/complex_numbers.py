# Reference: https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/

import cmath

def validate_complex(z):
    '''
    Ensures that the input is a complex, int, or float.
    '''
    if (not isinstance(z, (int, float, complex))):
        raise TypeError("Input must be an int, float, or complex number.")
    return complex(z)

# Addition of two complex numbers
def add_complex(z1, z2):
    z1, z2 = validate_complex(z1), validate_complex(z2)
    return z1 + z2

# Subtraction of two complex numbers
def subtract_complex(z1, z2):
    z1, z2 = validate_complex(z1), validate_complex(z2)
    return z1 - z2

# Multiplication of two complex numbers
def multiply_complex(z1, z2):
    z1, z2 = validate_complex(z1), validate_complex(z2)
    return z1 * z2

# Division of two complex numbers
def divide_complex(dividend_complex, divisor_complex):
    dividend_complex, divisor_complex = validate_complex(dividend_complex), validate_complex(divisor_complex)
    if (divisor_complex == 0):
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend_complex / divisor_complex

# Conjugate of a complex number
def conjugate_complex(z):
    z = validate_complex(z)
    return z.conjugate()

# Modulus (magnitude) of a complex number
def modulus_complex(z):
    z = validate_complex(z)
    return abs(z)

# Polar form (modulus and argument) of a complex number
def polar_complex(z):
    z = validate_complex(z)
    return cmath.polar(z)  # Returns (modulus, argument) as a tuple

# Exponentiation: raises a complex number to a power
def power_complex(complex_num, complex_exponent):
    complex_num, complex_exponent = validate_complex(complex_num), validate_complex(complex_exponent)
    if (complex_num == 0 and complex_exponent == 0):
        raise ValueError("0 raised to the 0 power is undefined.")
    return complex_num ** complex_exponent

# Square root of a complex number
def sqrt_complex(z):
    z = validate_complex(z)
    return cmath.sqrt(z)
