'''Find one missing number from 1 to 10

    >>> find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10])
    3

'''

def find_missing_number(list_numbers):
    
    if list_numbers[0] != 1:
        return 1
        
    for i in xrange(0, 10):
        if list_numbers[i + 1 ] != list_numbers[i] + 1:
            return list_numbers[i] + 1

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"