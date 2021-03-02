from itertools import permutations
from Nqueensmodule import *
import os
import sys

#n = int(input("Enter dimensions of chess board: "))
def board():
    chess = []
    for i in range(n):
        chess_inner = []
        for j in range(n):
            chess_inner.append("_")
        chess.append(chess_inner)
    return chess

def op(lst1):
    #l = board()
    new_b = []
    #for k in board:
    for i in lst1:
        l = board()
        #print(i)
        for j in i:
            #print(j)
            l[j[0]][j[1]] = "Q"
        #print(l)
        new_b.append(l)
    #print(new_b)
    print("The solutions are: \n")
    num = 1
    for i in new_b:
        print("Solution ", num)
        num += 1
        #print(i)
        for j in i:
            print(j)
        print("\n\n")
    """for i in range(n):
        for j in range(n):
            print(new_b[i], end = ' ')
        print("\n")"""

#To find queen config not in dale sequence
def dale_diag(lst):
    only_dale = []#Empty list that contains all queen arrangments that are now in dale config
    for queen in lst:
        #print(queen)
        lst_sum = []
        for i in range(n):
            sum = queen[i][0] - queen[i][1]
            lst_sum.append(sum)
        flag = 0
        for i in range(n):
            #flag = 0
            for j in range(i + 1, n):
                if (lst_sum[i] == lst_sum[j]):
                #print(sum[i], sum[j])
                    flag += 1
        if (flag == 0):
            only_dale.append(queen)

    #print(only_dale)
    return only_dale
        #sum = queen[0] - queen[1]
        #print(lst)
        #print(sum)

#To find queen config not in hill sequence
def hill_diag(lst):
    only_hill = []#Empty list that contains all queen arrangments that are now in hill config
    for queen in lst:
        #print(queen)
        lst_sum = []
        for i in range(n):
            sum = queen[i][0] + queen[i][1]
            lst_sum.append(sum)
        flag = 0
        for i in range(n):
            #flag = 0
            for j in range(i + 1, n):
                if (lst_sum[i] == lst_sum[j]):
                #print(sum[i], sum[j])
                    flag += 1
        if (flag == 0):
            only_hill.append(queen)

    return only_hill


def main():
    #n = int(input("Enter dimensions of chess board"))
    column =  range(n)
    #list_queens = []
    list_queens_final = []
    for i in permutations(column):
        list_queens = []
        #print(i)
        for j in range(n):
            queen_pos = [ j, i[j]]
            list_queens.append(queen_pos)
        #print(list_queens)
        list_queens_final.append(list_queens)
    #print(list_queens_final)

    dale = dale_diag(list_queens_final)
    hill = hill_diag(dale)
    if (len(hill) != 0):
        op(hill)
    else:
        print("No solution exists for {} Queen Problem".format(n))

def greater_than_9():
    #N=int(input('Enter the size of the board : '))
    N=n
    board=[[0 for i in range(N)] for i in range(N)]
    print('Your board : ')
    for i in range(N):
        for j in range(N):
            print(board[i][j],end='  ')
        print()
        print()

    if solveNQueens(board,0,N)==True:
        print('The solution to {} Queens problem is:'.format(N))
        for r in range(N):
            for c in range(N):
                print(board[r][c],end='  ')
            print()
            print()
    else:
        print('Impossible to solve\nThe Queens cannot be placed ')

def home_page():
    #import os
    welcome = "N-Queens Problem"
    print(welcome.center(100," "))
    description = """The N-Queens Problem is a classical problem of chess. Here N Queens are to be placed on an N * N chessboard \nin such a way that no queens attack each other. A Queen can attack other Queens if its placed on the same row,\ncolumn or on its diagonals. The solutions for the problem increases exponentially as n increases. Our project\ndisplays all the solutions for the problem upto n = 9. For any n greater, we have developed a code to provide\njust one solution satisfying the constraints. """
    print(description)
    clr = input("\nPress Enter to contine: ")
    if (clr != None):
        os.system('cls' if os.name == 'nt' else 'clear')

def check_n(n1):
    if (n1.isdigit() == True):
        #n1 = int(n1)
        return True
    else:
        return False

#board()
home_page()
loop = True
while loop:
    n = input("Enter dimensions of chess board: ")
    #print(check_n(n))
    if (check_n(n) == True):
        n = int(n)
        if (n <= 9):
            main()
        else:
            greater_than_9()
        print("Would you like to try again?\nPress y to continue and any other key to exit. ")
        c = input()
        if (c == 'y' or c == 'Y'):
            loop = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            loop = False
            sys.exit()
    else:
        print("Invalid input. \nPress y to try again or any other key to exit. ")
        choice = input()
        if (choice == 'y' or choice == 'Y'):
            loop = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            loop = False
            sys.exit()
