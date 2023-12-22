#!/usr/bin/python3
"""
determines if locked boxes in a sequence of size n
can all be opened if each box has a key to another box
"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened
    Args:
        boxes (list): list of lists of keys
    Returns:
       True if all boxes can be opened, False otherwise
    """
    opened = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key not in opened and key < len(boxes):
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == len(boxes)
