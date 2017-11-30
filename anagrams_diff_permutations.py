'''Cracking the Coding interview, problem 1.3:

Given two strings, write a method to decide if one is a permutation of the other.

Whitespace and punctuation are significant and it is case sensitive.

>>> sorted_anagram("nura", "arun")
True

>>> count_anagram("nura", "arun")
True

>>> sorted_anagram("Burger ", "Burger")
False

>>> count_anagram("Burger ", "Burger")
False

>>> sorted_anagram("RrRr", "rrrr")
False

>>> count_anagram("RrRr", "rrrr")
False

>>> sorted_anagram("Hello World!", "Hello World?")
False

>>> count_anagram("Hello World!", "Hello World?")
False

'''
from collections import Counter

# Option one - sorting first then comparing
def sorted_anagram(s1, s2):

    string1 = sorted(s1)
    string2 = sorted(s2)

    if len(string1) != len(string2):
        return False

    for indx in xrange(len(string1)):

        if string1[indx] != string2[indx]:
            return False

    return True

#Option two - counting first then comparing
def count_anagram(s1, s2):

    dict1 = Counter(s1)
    dict2 = Counter(s2)

    if len(s1) != len(s2):
        return False

    if dict1.keys() != dict2.keys():
        return False

    else:
        return True

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"