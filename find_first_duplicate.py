def firstDuplicate(a):
    '''Finds first duplicate number for which the second occurrence has the minimal index
    Uses O(n) time complexity and O(1) space complexity

    >>> a = [1, 2, 3, 3, 4, 2]
    3

    If there are no duplicates, return a -1
    >>> a = [1]
    -1
    '''
    
    seen = set()
    
    for num in a:
        
        if num in seen:
            return num
        
        else:
            seen.add(num)
    
    return -1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED.\n"
