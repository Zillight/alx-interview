#!/usr/bin/python3
"""
   Fewest number of coins needed from pile of coins
   to meet a given amount
"""


def makeChange(coins, total):
    """Returns fewest number of coins or -1 if not fulfiled"""
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    count = 0
    summation = 0
    for coin in coins:
        while summation < total:
            summation += coin
            count += 1
            if summation == total:
                return count
            if summation > total:
                summation -= coin
                count -= 1
                break
    return -1
