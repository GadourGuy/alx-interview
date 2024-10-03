#!/usr/bin/python3
"""
a function that prints pascal triangle
"""


from math import comb


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    else:
        L = []
        for i in range(n):
            L.append([comb(i, j) for j in range(i + 1)])
    return L
