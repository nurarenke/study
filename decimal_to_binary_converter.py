'''Convert a decimal to a binary number string

    >>> dec_to_bin(6)
    '110'

    >>> dec_to_bin(4)
    '100'

    >>> dec_to_bin(3)
    '11'

'''
def dec_to_bin(number):
    if number < 2: 
        return str(number)
    else:
        result = dec_to_bin(number/2) + dec_to_bin(number%2)
        return str(result)

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"