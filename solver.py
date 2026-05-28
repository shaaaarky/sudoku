"""
mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    """

mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]


def already_used_row(grid, row) -> list:
    # We need to scan the whole row
    used_in_row = []
    for elem in grid[row]: 
        if elem != 0 and elem not in used_in_row:
            used_in_row.append(elem)
    
    return used_in_row

def already_used_column(grid, col):
    used_in_col = []
    for i in range(9):
        # Check if the number isn't 0 or has appeared before 
        if grid[i][col] != 0 and grid[i][col] not in used_in_col: 
            used_in_col.append(grid[i][col])
    
    return used_in_col
        
def already_used_box(grid, row, col) -> list: 
    # Check if num exists in the 3x3 sub-matrix
    startRow = row - (row % 3)
    startCol = col - (col % 3)
    print(startRow, startCol)
    used_in_box = []
    for i in range(3):
        for j in range(3):
            if grid[startRow + i][startCol + j] != 0 and grid[startRow + i][startCol + j] not in used_in_box: 
               used_in_box.append(grid[startRow + i][startCol + j]) 
               
    return used_in_box

print(already_used_box(mat, 0, 0))
def solve(grid) -> list:
    pass