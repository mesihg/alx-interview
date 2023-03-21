#!/usr/bin/python3
"""
Coin change module
"""


def makeChange(coins, total):
    coins.sort(reverse=True)
    num_coins = 0
    remaining_amount = total
    for coin in coins:
        if coin <= remaining_amount:
            num_coins += remaining_amount // coin
            remaining_amount %= coin
    return num_coins
