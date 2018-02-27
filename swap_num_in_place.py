'''Write a function to swap a number in place (that is, without temporary variables).
From Cracking the coding interview 17.1

    >>> a = 9
    >>> b = 4

    >>> swap(a, b)
    ('a:', 4, 'b:', 9)

    >>> a = 1
    >>> b = 10

    >>> swap(a, b)
    ('a:', 10, 'b': 1

    >>> a = -3
    >>> b = 100

    >>> swap(a, b)
    a: 100, b: -3
'''
def swap(a, b):
    a = a - b 
    b = b + a 
    a = b - a

    return "a:", a, "b:", b

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
