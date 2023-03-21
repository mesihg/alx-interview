#!/usr/bin/python3
"""
Coin change module
"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total
    """
    if not coins or total < 0:
        return -1
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
