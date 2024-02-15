#!/usr/bin/python3

"""Making a change"""


def makeChange(coins, total):
    """
    this function returns, fewest number of coins needed to meet total
        If total =< 0 , return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1

    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change

    return -1