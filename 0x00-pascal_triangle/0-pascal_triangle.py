#!/usr/bin/python3

"""
Module of Pascal's triangle of size n
"""


def pascal_triangle(n):
    """Function returns a list of lists of integers
        representing the Pascal’s triangle of n.
    """

    if n <= 0:
        return []

    # Initialize empty triangle list
    triangle = []

    # Iterate through the rows(n)
    for i in range(n):
        current_row = []

        # Iterate through the column of the list[j is the index position]
        # # Row length is equal to it's row index plus 1
        for j in range(i + 1):

            # Check first and last elements of the Row
            if j == 0 or j == i:
                current_row.append(1)

            # Calculate and add inner elements
            else:
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                current_row.append(value)

        triangle.append(current_row)

    return triangle
