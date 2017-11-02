'''Find Missing Number from Pramp

Given an array of unique nonnegative integers, implement a function that 
finds the smallest nonnegative integer that is NOT in the array.

Assume the maximum value an integer can have is MAX_INT = 2^31 - 1.

Tests:

>>> arr = [0, 1, 2, 3]
>>> find_missing_num(arr)
4

>>> arr = [0, 1, 3, 4]
>>> find_missing_num(arr)
2

'''

def find_missing_num(arr):
    seen = set(arr)
    number = 0
    MAX_INT = (2**31) - 1

    while number <= MAX_INT:
        if number not in seen:
            return number
        else:
            number += 1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.\n"
