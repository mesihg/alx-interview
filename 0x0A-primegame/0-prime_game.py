#!/usr/bin/python3
""" Prime Game Module """


def isWinner(x, nums):
    """ Return name of the player that won the most rounds """
    def dp(state, player):
        if state.count(True) == 0:
            return False
        if player in memo[state]:
            return memo[state][player]
        result = False
        for p in primes:
            if state[p]:
                new_state = [True] * len(state)
                for i in range(p, len(state), p):
                    new_state[i] = False
                other_player = not player
                if not dp(tuple(new_state), other_player):
                    result = True
                    break
        memo[state][player] = result
        return result
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False
    primes = [i for i in range(2, max_num + 1) if sieve[i]]
    memo = {}
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        state = tuple([True] * (n + 1))
        memo[state] = {}
        winner = "Maria" if dp(state, True) else "Ben"
        wins[winner] += 1
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
