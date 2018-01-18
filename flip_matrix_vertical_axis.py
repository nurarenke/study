'''You are given an m x n 2D image matrix (List of Lists) 
where each integer represents a pixel. Flip it in-place along
its vertical axis.

    >>> matrix = [[1,0],[1,0]]
    >>> flip_vertical_axis(matrix)
    [[0, 1], [0, 1]]

    >>> matrix = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
    >>> flip_vertical_axis(matrix)
    [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

'''
def flip_vertical_axis(matrix):
    
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

    return matrix

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"