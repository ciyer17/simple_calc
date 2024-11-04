from calculator import *

# Test cases for each function with expected results

print("Basic Operations:")
# Test case for addition
params = (5, 3)
print(f"Addition; Arguments: {params}; Expected: 8; Actual: {add(*params)}")

# Test case for subtraction
params = (10, 4)
print(f"Subtraction; Arguments: {params}; Expected: 6; Actual: {subtract(*params)}")

# Test case for multiplication
params = (7, 6)
print(f"Multiplication; Arguments: {params}; Expected: 42; Actual: {multiply(*params)}")

# Test case for division
params = (8, 2)
print(f"Division; Arguments: {params}; Expected: 4.0; Actual: {divide(*params)}")

print("\nAdvanced Operations")

# Test case for power
params = (2, 3)
print(f"Power; Arguments: {params}; Expected: 8; Actual: {power(*params)}")

# Test case for square root
params = (16)
print(f"Square Root; Arguments: {params}; Expected: 4.0; Actual: {square_root(params)}")

# Test case for factorial
params = (5)
print(f"Factorial; Arguments: {params}; Expected: 120; Actual: {factorial(params)}")

print("\nLogarithms")

# Test case for logarithm
params = (100, 10)
print(f"Logarithm; Arguments: {params}; Expected: 2.0; Actual: {logarithm(*params)}")

# Test case for natural log
params = (math.e)
print(f"Natural Log; Arguments: {params}; Expected: 1.0; Actual: {natural_log(params)}")

# Test case for exponential
params = (2)
print(f"Exponential; Arguments: {params}; Expected: {round(math.exp(params), 2)}; Actual: {exponential(params)}")

print("\nTrignometry")

# Test case for sine
params = (math.pi / 2)  # Sine of 90 degrees (π/2 radians)
print(f"Sine; Arguments: {params}; Expected: 1.0; Actual: {sin(params)}")

# Test case for cosine
params = (0)  # Cosine of 0 radians
print(f"Cosine; Arguments: {params}; Expected: 1.0; Actual: {cosine(params)}")

# Test case for tangent
params = (math.pi / 4)  # Tangent of 45 degrees (π/4 radians)
print(f"Tangent; Arguments: {params}; Expected: 1.0; Actual: {tangent(params)}")

print("\nStatistics")

# Test case for mean
params = [1, 2, 3, 4, 5]  # Mean of the list
print(f"Mean; Arguments: {params}; Expected: 3; Actual: {mean(params)}")

# Test case for median
params = [1, 2, 3, 4, 5]  # Median of the list
print(f"Median; Arguments: {params}; Expected: 3; Actual: {median(params)}")

# Test case for mode
params = [1, 2, 2, 3, 4]  # Mode of the list
print(f"Mode; Arguments: {params}; Expected: 2; Actual: {mode(params)}")

# Test case for standard deviation
params = [1, 2, 3, 4, 5]  # Standard deviation of the list
print(f"Standard Deviation; Arguments: {params}; Expected: 1.58; Actual: {standard_deviation(params)}")

print("\nComplex Numbers")

# Test case for addition of complex numbers
params = (1 + 2j, 3 + 4j)  # Adding two complex numbers
print(f"Addition; Arguments: {params}; Expected: (4+6j); Actual: {add_complex(*params)}")

# Test case for subtraction of complex numbers
params = (5 + 3j, 2 + 1j)  # Subtracting two complex numbers
print(f"Subtraction; Arguments: {params}; Expected: (3+2j); Actual: {subtract_complex(*params)}")

# Test case for multiplication of complex numbers
params = (2 + 3j, 4 + 5j)  # Multiplying two complex numbers
print(f"Multiplication; Arguments: {params}; Expected: (-7 + 22j); Actual: {multiply_complex(*params)}")

# Test case for division of complex numbers
params = (4 + 2j, 2 + 1j)  # Dividing two complex numbers
print(f"Division; Arguments: {params}; Expected: (2.0 + 0.0j); Actual: {divide_complex(*params)}")

# Test case for conjugate of a complex number
params = (3 + 4j)  # Conjugate of the complex number
print(f"Conjugate; Arguments: {params}; Expected: (3 - 4j); Actual: {conjugate_complex(params)}")

# Test case for modulus of a complex number
params = (3 + 4j)  # Modulus of the complex number
print(f"Modulus; Arguments: {params}; Expected: 5.0; Actual: {modulus_complex(params)}")

# Test case for polar form of a complex number
params = (1 + 1j)  # Polar form of the complex number
print(f"Polar Form; Arguments: {params}; Expected: (1.4142135623730951, 0.7853981633974483); Actual: {polar_complex(params)}")

# Test case for exponentiation of a complex number
params = (1 + 1j, 2)  # Raising a complex number to a power
print(f"Exponentiation; Arguments: {params}; Expected: (2j); Actual: {power_complex(*params)}")

# Test case for square root of a complex number
params = (1 + 1j)  # Square root of the complex number
print(f"Square Root; Arguments: {params}; Expected: (1.09868411346781 + 0.45508986056222733j); Actual: {sqrt_complex(params)}")
