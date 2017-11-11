'''DFS thru connected Grid from Hackerrank problem
https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem

Consider a matrix with  rows and  columns, where each cell contains either a 
or 1 a 0 and any cell containing a 1 is called a filled cell. Two cells are said to 
be connected if they are adjacent to each other horizontally, vertically, or diagonally.

If one or more filled cells are also connected, they form a region. 
Note that each cell in a region is connected to at least one other cell in the region 
but is not necessarily directly connected to all the other cells in the region.

>>> the_grid = [[1, 1, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 0]]
>>> find_biggest_region(the_grid)
6

>>> the_grid = [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
>>> find_biggest_region(the_grid)
5

>>> the_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
>>> find_biggest_region(the_grid)
0

>>> the_grid = [[1]]
>>> find_biggest_region(the_grid)
1

'''
def find_biggest_region(grid):
    num_row = len(grid)
    num_col = len(grid[0])

    visited = set()
    biggest_region = 0

    for row in xrange(num_row):
        for col in xrange(num_col):

            # if the element equals 1, we depth first search all of their neighbors
            # then return size of that particual region
            if grid[row][col] == 1 and grid[row][col] not in visited:
                size_of_region = dfs_search(grid, row, col, visited, num_row, num_col)

                # we keep track of that region 
                if size_of_region > biggest_region:
                    biggest_region = size_of_region

    return biggest_region


def dfs_search(grid, row, col, visited, num_row, num_col):

    # keep track of the original visited length
    original_visited_size = len(visited)
    
    # evertime you see a 1, you add it to visited
    visited.add((row, col))

    # check all around each element
    for neighbor_row in xrange(row-1, row+2):
        for neighbor_col in xrange(col-1, col+2):

            # this is prevent you from getting an index error
            if neighbor_row < num_row and neighbor_row >= 0 and neighbor_col < num_col and neighbor_col >= 0:
                # if the elemnt is a 1 and we haven't visited yet, we repeat the process again
                if grid[neighbor_row][neighbor_col] == 1 and (neighbor_row, neighbor_col) not in visited:
                    dfs_search(grid, neighbor_row, neighbor_col, visited, num_row, num_col)

    # now we check the current length of visited with the original 
    return len(visited) - original_visited_size

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"

          
