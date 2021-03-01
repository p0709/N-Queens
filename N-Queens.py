from itertools import permutations

n = int(input("Enter dimensions of chess board: "))
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
    op(hill)
#board()
main()
