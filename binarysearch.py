"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""
    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 1

    low = 0 
    mid = 50
    high = 100

    while val != mid:
       
        if val > mid:
            low = mid + 1

        else:
            high = mid

        mid = (low + high) / 2

        num_guesses += 1

    return num_guesses

def binary_search_names(names, name):
    '''Return the index if the name exists in the list of names, otherwise return None. Names is sorted.

    >>> names = ['alice', 'burger', 'chris', 'nura', 'phil', 'spice', 'ticket', 'trout', 'wineosaurus']
    >>> binary_search_names(names, "alice")
    0

    >>> binary_search_names(names, "dude")
    False

    >>> binary_search_names(names, "zzzz")
    False

    >>> binary_search_names(names, "aaaa")
    False

    >>> binary_search_names(names, "pppppp")
    False

    >>> binary_search_names(names, "trout")
    7
    '''

    low = 0
    high = len(names) - 1
    mid = (low + high) / 2

    while name != names[mid]:

        if low == high:
            return False


        if name > names[mid]:
            low = mid + 1

        else:
            high = mid

        mid = (low + high) / 2

    return mid


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"
