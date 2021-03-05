def is_safe(board,row,col,n):
    for i in range(col,-1,-1):
        if board[row][i]==1:
            return False
    r=row
    c=col
    while r<n and c>=0:
        if board[r][c]==1:
            return False
        r+=1
        c-=1
    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    return True

def solveNQueens(board,col,n):
    if col==n:
        return True
    for i in range(n):
        if is_safe(board,i,col,n):
            board[i][col]=1
            if solveNQueens(board,col+1,n):
                return True
            board[i][col]=0
    return False

        
                
