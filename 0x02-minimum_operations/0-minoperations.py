#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Function that calculates the minimum number of operations to
    copy and paste a number
    """
    operations = 0   # Initialize the operation count
    current = 1      # Initialize the current value
    clipboard = 0    # Initialize the value in the clipboard

    # Continue looping until the current value reaches or exceeds n
    while current < n:
        if n % current == 0:
            # If the current value is a factor of n, perform a Copy operation
            clipboard = current   # Store the current value in the clipboard
            current *= 2          # Double the current value
            operations += 1       # Increment the operation count (Copy)
        else:
            # If the current value is not a factor of n, perform a Paste operation
            current += clipboard  # Add the value in the clipboard to the current value
        operations += 1           # Perform a Paste operation in either case

    return operations