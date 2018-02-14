from itertools import groupby 
'''
Write a method that would take in a list of words and return a list of anagrams.

    >>> words = ['cat', 'dog', 'tac', 'god', 'act']
    >>> return_anagrams(words)
    [['dog', 'god'], ['cat', 'tac', 'act']]

'''



def return_anagrams(words):
    for _, group in groupby(sorted(words, key=sorted), sorted):
        group = list(group)
        if len(group) > 1:
            return group


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"