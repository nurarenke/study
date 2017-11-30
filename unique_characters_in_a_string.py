''' Unique Characters in a string from cracking the coding interview, problem 1.1

Implement an algorithm to determine if a string has all unique characters. What if
you cannot use additional data structures?

>>> s = "Burger is cool"
>>> unique_char(s)
False

>>> s = "Nura"
>>> unique_char(s)
True

'''

# Time complexity of O(n^2)

def unique_char(s):

    string = s.strip().lower()

    length = len(string)

    for i in xrange(length):
        for n in xrange(i + 1, length):
            if string[i] == string[n]:
                return False
                
    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"