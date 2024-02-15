#!/usr/bin/python3
"""check for the winner of the prime game
"""


def isWinner(x, nums):
    """Return the winner of the prime game
    """
    primes = [2]

    def isPrime(x):
        """Return whether a number is prime or not
        """
        if x < 2:
            return False
        if x in primes:
            return True
        if primes[-1] > x:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        primes.append(x)
        return True

    def pickPrimeAndFactors(lst):
        """Remove 1st prime number in a list & factors
        """
        prime = None
        for i in lst:
            if isPrime(i):
                prime = i
                break

        if prime is None:
            return None

        return [i for i in lst if i % prime != 0]

    players = [0, 0]

    for i in range(x):
        turn = 0
        n = list(range(1, nums[i] + 1))

        while True:
            n = pickPrimeAndFactors(n)
            turn += 1
            if n is None:
                players[(turn) % 2] += 1
                break

    if players[0] > players[1]:
        return "Maria"
    elif players[1] > players[0]:
        return "Ben"

    return None
