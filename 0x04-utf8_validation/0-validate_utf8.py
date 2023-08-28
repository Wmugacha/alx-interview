#!/usr/bin/python3
"""
UTF-8 encoding module
"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""

    for byte in data:
        if byte < 0 or byte > 255:
            return False
    return True
