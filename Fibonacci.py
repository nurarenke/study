"""Recursion

    >>> fib_recurse(0)
    0
    >>> fib_recurse(1)
    1
    >>> fib_recurse(10)
    55
"""

def fib_recurse(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recurse(n-1) + fib_recurse(n-2)

"""Dynamic Programming
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)
    55
"""
def fib(n):
    twoBack = 0
    oneBack = 1
    if n < 2:
        return n
        
    for i in range(1, n):
        newNum = oneBack + twoBack
        twoBack = oneBack
        oneBack = newNum

    return oneBack

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"