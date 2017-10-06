from collections import defaultdict

"""Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid 
with numbers in such a way that each column, each row, and each of the nine 
3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of
numbers represents a valid Sudoku puzzle according to the layout 
rules described above. Note that the puzzle represented by grid does not have to be solvable.


The problem is from Codefights

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

    >>>sudoku2(grid)
    True
"""

def sudoku2(grid):
    squares = defaultdict(set)
    rowSet = defaultdict(set)
    colSet = defaultdict(set)
    for rowInd, row in enumerate(grid):
        for colInd, value in enumerate(row):
            if value == ".": continue
            square = (rowInd / 3, colInd / 3)
            if value in squares[square]:
                return False
            if value in rowSet[rowInd]:
                return False
            if value in colSet[colInd]:
                return False
            colSet[colInd].add(value)
            rowSet[rowInd].add(value)
            squares[square].add(value)
            
    return True

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED;\n"
