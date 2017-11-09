'''Connected Cell in a Grid Problem from Hackerrank

Consider a matrix with  rows and  columns, where each cell contains either a  or a  and any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally; in other words, cell  is connected to cells , , , , , , , and , provided that the location exists in the matrix for that .

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.

Task 
Given an  matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.

Input Format

The first line contains an integer, , denoting the number of rows in the matrix. 
The second line contains an integer, , denoting the number of columns in the matrix. 
Each line  of the  subsequent lines contains  space-separated integers describing the respective values filling each row in the matrix.
'''
def get_biggest_region(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    sets_of_cells = []
    
    for row in xrange(num_rows):
        for col in xrange(num_cols):
            if grid[row][col] == 1:
                
                print "1 @  ", row, col
                neighbor_cells = set()
                print "neighbor_cells before", neighbor_cells
                
                for neighbor_row in xrange(row-1, row+2):
                    for neighbor_col in xrange(col-1, col+2):
                        
                        # protect against index error by checking first if you're
                        # at the end of the grid
                        if neighbor_row < num_rows and neighbor_row >= 0 and neighbor_col < num_cols and neighbor_col >= 0:
                            if grid[neighbor_row][neighbor_col] == 1:
                                neighbor_cells.add((neighbor_row, neighbor_col))
                                print "neighbor_cells added", neighbor_cells
            
            print "neighbor_cell all finished", neighbor_cells  
            added_to_existing = False
            print "set of cells before", sets_of_cells
            for set_of_cells in sets_of_cells:
                if not set_of_cells.isdisjoint(neighbor_cells):
                    set_of_cells.update(neighbor_cells)
                    added_to_existing = True
                    break
                    
            if not added_to_existing:
                sets_of_cells.append(neighbor_cells)
            
    return max(len(x) for x in sets_of_cells)
            
    

the_grid = [[1, 1, 0, 1],
 [0, 1, 1, 1],
 [0, 0, 0, 0],
 [0, 0, 0, 1],
 [1, 1, 1, 0]]

print get_biggest_region(the_grid)

