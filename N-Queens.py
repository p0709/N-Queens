from itertools import permutations
from Nqueensmodule import *
import os
import sys

#Function to create empty chess board
def board():
    chess = []

    for i in range(n):
        chess_inner = []
        for j in range(n):
            chess_inner.append("_")
        chess.append(chess_inner)

    return chess

#Function to place queens in the appropriate positions according to the constraints
def op(lst1):
    new_b = []

    #For loop to place the queens in the appropriate position for each solution
    for i in lst1:
        l = board()
        for j in i:
            l[j[0]][j[1]] = "Q"
        new_b.append(l)

    print("The solutions are: \n")
    num = 1
    #For loop to print solutions
    for i in new_b:
        print("Solution", num)
        num += 1
        for j in i:
            print(" ".join(j))
        print("\n\n")

#To find queen config not in dale sequence - difference of indexes for a queen in the dale diagnal is the same for all queens in the diagnal
def dale_diag(lst):
    only_dale = []#Empty list that contains all queen arrangments that are now in dale config
    #For loop to create list containing difference of indexes of each queen

    for queen in lst:
        lst_diff = []
        for i in range(n):
            diff = queen[i][0] - queen[i][1]
            lst_diff.append(diff)

        flag = 0
        #For loop to check if the differrence of indexes of any two queens are equal
        for i in range(n):
            for j in range(i + 1, n):
                if (lst_diff[i] == lst_diff[j]):
                    flag += 1

        #If indexes are difference of indexes are equal for any two queens, then that permutation is not a part of the solution set
        if (flag == 0):
            only_dale.append(queen)

    return only_dale

#To find queen config not in hill sequence - sum of indexes for a queen in the dale diagnal is the same for all queens in the diagnal
def hill_diag(lst):
    only_hill = []#Empty list that will contain all queen arrangments that are now in hill config
    #For loop to create list containing sum of indexes of each queen

    for queen in lst:
        lst_sum = []
        for i in range(n):
            sum = queen[i][0] + queen[i][1]
            lst_sum.append(sum)

        flag = 0
        #For loop to check if the sum of indexes of any two queens are equal
        for i in range(n):
            for j in range(i + 1, n):
                if (lst_sum[i] == lst_sum[j]):
                    flag += 1

        #If indexes are sum of indexes are equal for any two queens, then that permutation is not a part of the solution set
        if (flag == 0):
            only_hill.append(queen)

    return only_hill

#Function to find and append in a list all possible permutations of positions of queens in each row
def main():
    column =  range(n)
    list_queens_final = []#List to contain all possible solution configurations

    #For loop to append all possible queen positions with one queen in each row into a list
    for i in permutations(column):
        list_queens = []
        for j in range(n):
            queen_pos = [ j, i[j]]
            list_queens.append(queen_pos)
        list_queens_final.append(list_queens)

    dale = dale_diag(list_queens_final)
    #Hill_diag fn is called on the list with more than one queens that are not on the dale diagnal
    hill = hill_diag(dale)

    #If the lenght of the operated list is zero, no solution exists, else op fn is called
    if (len(hill) != 0):
        op(hill)
    else:
        print("No solution exists for {} Queen Problem".format(n))

#Fn to find one solution for n values frater than 9
def greater_than_9():
    N = n
    board=[["_" for i in range(N)] for i in range(N)]#To create empty chess board

    #Solve queens fn imported from Nqueensmodule
    if solveNQueens(board,0,N)==True:
        print('The solution to {} Queens problem is:\n'.format(N))
        #For loop to print solution
        for r in range(N):
            for c in range(N):
                print(board[r][c],end='  ')
            print()
        print()
    else:
        print('Impossible to solve\nThe Queens cannot be placed ')

#Fn to display introductory page
def home_page():
    welcome = "N-Queens Problem"
    print(welcome.center(100," "))

    description = """The N-Queens Problem is a classical problem of chess. Here N Queens are to be placed on an N * N chessboard \nin such a way that no queens attack each other. A Queen can attack other Queens if its placed on the same row,\ncolumn or on its diagonals. The solutions for the problem increases exponentially as n increases. Our project\ndisplays all the solutions for the problem upto n = 9. For any n greater, we have developed a code to provide\njust one solution satisfying the constraints. """
    print(description)

    clr = input("\nPress Enter to continue: ")
    if (clr != None):
        os.system('cls' if os.name == 'nt' else 'clear')#To clear the output screen

#Fn to check if n value is in the accepted format
def check_n(n1):
    if (n1.isdigit() == True and (int(n1) > 0 and int(n1) <= 20) ):
        return True

    elif (n1.isdigit() == True and (int(n1) > 20 or int(n1) == 0)):
        print("n value out of range(valid range: 1 to 20).\nPress y to try again or any other key to exit.")
        return False

    else:
        return False

home_page()


loop = True
while loop:
    n = input("Enter dimensions of chess board(valid range: 1 to 20): ")

    if (check_n(n) == True):
        n = int(n)

        if (n <= 9):
            main()
        else:
            greater_than_9()

        print("Would you like to try again?\nPress y to continue or any other key to exit. ")
        c = input()

        if (c == 'y' or c == 'Y'):
            loop = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            loop = False
            sys.exit()

    else:
        if (n.isdigit() != True):
            print("Invalid input. \nPress y to try again or any other key to exit. ")
        choice = input()
        if (choice == 'y' or choice == 'Y'):
            loop = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            loop = False
            sys.exit()
