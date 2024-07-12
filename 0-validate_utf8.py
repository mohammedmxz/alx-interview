#!/usr/bin/python3
"""
Define validUTF8 function.
"""


def validUTF8(data):
    """
    Check if the given data is a valid UTF-8 encoding.
    """
    chunk = 1

    for item in data:
        if chunk == 1:
            if item >> 5 == 0b110:
                chunk = 2
            elif item >> 4 == 0b1110:
                chunk = 3
            elif item >> 3 == 0b11110:
                chunk = 4
            elif item >> 7 & 0b1:
                return False
        else:
            if item >> 6 != 0b10:
                return (False)

            chunk -= 1

    return chunk == 1
