from collections import defaultdict

'''Sudoku is a number-placement puzzle. The objective is to fill a 9 by 9 grid 
with numbers in such a way that each column, each row, and each of the nine 
3 by 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of
numbers represents a valid Sudoku puzzle according to the layout 
rules described above. Note that the puzzle represented by grid does not have to be solvable.


The problem is from Codefights

    >>> grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
                ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
                ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
                ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
                ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
                ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
                ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

    >>> sudoku2(grid)
    True
'''
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
                ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
                ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
                ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
                ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
                ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
                ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

def sudoku2(grid):
    squares = defaultdict(set)
    print "squares", squares
    rowSet = defaultdict(set)
    print "rowSet", rowSet
    colSet = defaultdict(set)
    print "colSet",
    for rowInd, row in enumerate(grid):
        print "rowInd", rowInd, 
        print "row", row
        for colInd, value in enumerate(row):
            print "colInd", colInd
            print "value", value
            if value == ".": continue
            square = (rowInd / 3, colInd / 3)
            print "square", square
            if value in squares[square]:
                print "squares[square]", squares[square]
                return False
            if value in rowSet[rowInd]:
                print "rowSet[rowInd]", rowSet[rowInd]
                return False
            if value in colSet[colInd]:
                print "colSet[colInd]", colSet[colInd]
                return False
            print "colSet before", colSet
            colSet[colInd].add(value)
            print "colSet after", colSet
            print "rowSet before", rowSet
            rowSet[rowInd].add(value)
            print "rowSet after", rowSet
            print "squares before", squares
            squares[square].add(value)
            print "squares after", squares
            
    return True

if __name__ == "__main__":
    sudoku2(grid)
    # import doctest
    # if doctest.testmod().failed == 0:
    #     print "\n*** ALL TESTS PASSED;\n"
