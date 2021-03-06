#Fn to check if queen can be placed at the given position
def is_safe(board,row,col,n):
    #For loop to check if the row on the left of the given row is safe
    for i in range(col,-1,-1):
        if board[row][i]=="Q":
            return False

    r=row
    c=col
    #While loop to check is lower diagnal is safe
    while r<n and c>=0:
        if board[r][c]=="Q":
            return False
        r+=1
        c-=1

    i=row
    j=col
    #While loop to check if upper diagnal is safe
    while i>=0 and j>=0:
        if board[i][j]=="Q":
            return False
        i-=1
        j-=1

    return True

#Fn to place queens in the required positions
def solveNQueens(board,col,n):
    #Base condition for recursion
    if col == n:
        return True

    #Recursive loop to place a queen satisfying all constraints in each column
    for i in range(n):
        if is_safe(board,i,col,n):
            board[i][col]="Q"
            if solveNQueens(board,col+1,n):
                return True
            board[i][col]="_"

    return False
