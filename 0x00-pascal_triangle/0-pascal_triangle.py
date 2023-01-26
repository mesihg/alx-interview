#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    return list of lists of integers
    """
    if n <= 0:
        return []
    res = [[1] * i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res
