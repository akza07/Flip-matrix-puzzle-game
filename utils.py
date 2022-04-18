# Read matrix
def read_matrix():
    mat = []
    [row, column] = map(int, input(
        "Enter row and column (Eg : '3x3') : ").split("x"))
    print("Now enter the matrix, separated by space\nEach row in new line : ")
    for i in range(row):
        mat.append(
            list(input().split(" "))
        )
    return mat

# Display the matrix
def show_matrix(mat):
    print("Matrix now :")
    for row in mat:
        print(row)
        # print("\n")

# Flip row
def flip_row(mat, row):
    if row > len(mat):
        print(f"Wait wait wait, we only have {len(mat[0])} rows")
        print(f"[WARNING] You're losing IQ")
    else:
        print("Flipped row")
        mat[row-1].reverse()
        return mat

# Flip column
def flip_column(mat, column):
    column = column - 1
    if column > len(mat):
        print(f"Hmm... You do know we have just {len(mat)} columns")
        print(f"[WARNING] You're losing IQ")
    else:
        length = len(mat)-1
        for i in range((length+1)//2):
            temp = mat[i][column]
            mat[i][column] = mat[length-i][column]
            mat[length-i][column] = temp
            print("Flipped column")
        return mat

from random import randint
def shuffle_mat(mat):
    shuffle_actions = []
    direction = ['R','C']
    length = len(mat)
    for i in range( length+1 ):
        action = randint(1,length)
        what_to_flip = randint(0,1)
        if action not in shuffle_actions:
            shuffle_actions.append(f"{direction[what_to_flip]}{action}")
    for item in shuffle_actions:
        if item[0] == 'R':
            flip_row(mat,int(item[1:]))
        else:
            flip_column(mat,int(item[1:]))
    return [mat,list(set(shuffle_actions))]