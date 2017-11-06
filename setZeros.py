'''Cracking the Coding Interview Problem 1.7

Write an algorithm such that if an element in an MxN matrix is 0, its
entire row and column are set to 0.

>>> matrix = [[1, 0, 1, 1, 0], 
            [0, 1, 1, 1, 0], 
            [1, 1, 1, 1, 1], 
            [1, 0, 1, 1, 1], 
            [1, 1, 1, 1, 1]]

>>> set_zeros(matrix)
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0]]

'''

def set_zeros(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    for row_index in rows:
        for i in range(len(matrix[0])):
            matrix[row_index][i] = 0

    for col_index in cols:
        for i in range(len((matrix))):
            matrix[i][col_index] = 0 


    return matrix

    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"