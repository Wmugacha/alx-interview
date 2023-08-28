#!/usr/bin/python3
"""
UTF-8 encoding module
"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""

    i = 0
    while i < len(data):
        integer = data[i]

        if integer < 0 or integer > 255:
            return False  # Each integer should be a valid byte (0 to 255)

        byte = bytes([integer])[0]  # Convert integer to bytes

        if byte & 0x80 == 0x00:
            # ASCII character
            i += 1
        elif byte & 0xE0 == 0xC0:
            # Two-byte character
            # Validate continuation byte
            if i + 1 >= len(data) or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        elif byte & 0xF0 == 0xE0:
            # Three-byte character
            # Validate continuation bytes
            if i + 2 >= len(data):
                return False
            for j in range(i + 1, i + 3):
                if j >= len(data) or data[j] & 0xC0 != 0x80:
                    return False
            i += 3
        elif byte & 0xF8 == 0xF0:
            # Four-byte character
            # Validate continuation bytes
            if i + 3 >= len(data):
                return False
            for j in range(i + 1, i + 4):
                if j >= len(data) or data[j] & 0xC0 != 0x80:
                    return False
            i += 4
        else:
            return False  # Invalid byte pattern

    return True
