#!/usr/bin/python3
"""
Method that determines if a given data set represents
a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Returns: True if data is a valid UTF-8 encoding,
    else return False
    A character in UTF-8 can be 1 to 4 bytes long
    """
    bytes = 0
    for num in data:
        bitcodes = format(num, '#010b')[-8:]
        if bytes == 0:
            for bit in bitcodes:
                if bit == '0':
                    break
                bytes += 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (bitcodes[0] == '1' and bitcodes[1] == '0'):
                return False
        bytes -= 1
    return bytes == 0
