#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is to be calculated.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the given number.
             Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the input number from the command-line arguments
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)

