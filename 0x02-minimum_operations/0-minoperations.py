#!/usr/bin/python3
"""minimum opertions"""


def minOperations(n):
    """
    This function gets fewest num  of operations needed to result in exactly n H characters
    """
    # it is impossible to achieve a value lower than 2 because the n of operations copy and paste
    # threfore 0 is returned
    if (n < 2):
        return 0
    ops_count = 0
    root_div = 2
    while root_div <= n:
        # if n evenly divides by root_div
        if n % root_div == 0:
            ops_count += root_div
            n = n / root_div
            root_div -= 1
        root_div += 1
    return ops_count