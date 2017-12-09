'''Cracking the Coding Interview Problem 1.6.

Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, white a method to rotate the image by 90 degrees. Ca you do this in place?

>>> grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> rotate(grid)
[(7, 4, 1), (8, 5, 2), (9, 6, 3)]

'''

def rotate(grid):

    return zip(*grid[::-1])

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"