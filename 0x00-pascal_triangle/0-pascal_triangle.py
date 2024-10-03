#!/usr/bin/python3
"""
a function that prints pascal triangle
"""


def fact(n):
    """ function to count factorial
    """
    if n == 0 or n == 1:
        return 1
    res = 1

    for i in range(2, n+1):
        res = res * i

    return res


def nCr(n, r):
    """ function to count nCr"""
    return (fact(n) // (fact(r) * fact(n - r)))


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    else:
        L = []
        for i in range(n):
            L.append([nCr(i, j) for j in range(i + 1)])
    return L
