'''
Valid Sudoku
'''

"Algorithm 1 using set/hash-set"

board = [
    ['7','5','.','.','.','.','4','.','9'],
    ['1','2','.','.','.','.','4','.','9'],
    ['3','.','.','.','.','.','4','.','9'],
    ['6','4','.','.','.','.','4','.','9'],
    ['2','.','.','.','.','.','4','.','9'],
    ['.','8','.','.','.','.','4','.','9'],
    ['.','1','.','.','.','.','4','.','9'],
    ['4','5','.','.','.','.','4','.','9'],
    ['.','5','.','.','.','.','4','.','9'],
]

def is_valid_sud(board):
    seen = set()
    for i in range(0,9):
        for j in range(0,9):
            current_val = board[i][j]
            if( current_val != '.'):
                curr_val_rows = '{curr_val} found in rows {i}'.format(curr_val = current_val, i=i)
                curr_val_cols = '{curr_val} found in cols {j}'.format(curr_val = current_val, j=j)
                curr_val_grids = '{curr_val} found in grid {i}-{j}'.format(curr_val = current_val, i=i//3,j=j//3)
                if (curr_val_rows not in seen or curr_val_cols not in seen or curr_val_grids not in seen):
                    seen.add(curr_val_rows)
                    seen.add(curr_val_cols)
                    seen.add(curr_val_grids)
                else: 
                    return False
    return True                


print(board,"\nResult : ",is_valid_sud(board))
print('-'*40)

board_2 = [[ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],  
             [ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],  
             [ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],  
             [ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],  
             [ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],  
             [ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],  
             [ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],  
             [ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],  
             [ '.', '.', '.', '.', '8', '.', '.', '7', '9' ]] 

print(board_2,"\nResult : ",is_valid_sud(board_2))