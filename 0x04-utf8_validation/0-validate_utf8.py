#!/usr/bin/python3
"""
UTF-8 encoding module
"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""

    # Variable to keep track of the number of bytes
    remaining_bytes = 0

    # Masks for checking valid byte patterns (10xxxxxx)
    continuation_mask_1 = 1 << 7
    continuation_mask_2 = 1 << 6

    for byte_value in data:

        byte_mask = 1 << 7

        if remaining_bytes == 0:
            # Determine the number of bytes the UTF-8 character will have
            while byte_mask & byte_value:
                remaining_bytes += 1
                byte_mask = byte_mask >> 1

            # If the byte count did not increase, it's a 1-byte character
            if remaining_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            # Continuation bytes should start with 10
            if not (byte_value & continuation_mask_1 and not
                    (byte_value & continuation_mask_2)):
                return False

        # Decrement the byte count as we process each byte of the character
        remaining_bytes -= 1

    # All characters were verified correctly with their proper byte count
    if remaining_bytes == 0:
        return True

    return False
