'''Cracking the Coding Interview problem 1.5

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become 
a2b1c5a3. If the compressed string would not become smaller than the orginal
string, your method should return the original string.

>>> compressed_string("aabcccccaaa")
'a2b1c5a3'

>>> compressed_string("abc")
'abc'

>>> compressed_string('')
''
'''

# is the next character the same, then add to the count
# if the next character is not the same, then append the count 

def compressed_string(s):

    count = 1

    string_to_print = ""

    for indx in xrange(len(s)):

        if indx < (len(s) - 1) and s[indx] == s[indx + 1]:
            count += 1

        if indx < (len(s) - 1) and s[indx] != s[indx + 1]:
            string_to_print += s[indx]
            string_to_print += str(count)
            count = 1
        
        if indx == len(s) - 1:
            string_to_print += s[indx]
            string_to_print += str(count)


        if len(string_to_print) / 2 == len(s):
            return s 

    return string_to_print

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"