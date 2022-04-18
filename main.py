from sqlalchemy import null
from utils import *

intro = """
------FLIP-MY-MATRIX------

Q. What is this game?
Ans.You enter the Dimensions, Enter the matrix, It shuffles
by flipping rows and columns, you fix it in an efficient way.

Setps will be counted.
"""

print(intro)
arr = read_matrix()
[arr,solution]=shuffle_mat(arr)
print(f"{solution=}")
show_matrix(arr)

prompt = """
Q. How to flip?
Ans. If you want to flip, enter the row or column as
'R(no)' or C(no) and that will be flipped
'Q' for Quit"""

print(prompt)
history = []
while(True):
    value = input("Flip : ")
    if value == "Q":
        print("See ya later... Bye Bye!")
        break
    elif value[0] in ["R","r"]:
        arr = flip_row(arr, int(value[1:]))
        show_matrix(arr)
        history.append(value)
        print(f"History = {history}")

    elif value[0] in ["C","c"]:
        arr = flip_column(arr, int(value[1:]))
        show_matrix(arr)
        history.append(value)
        print(f"History = {history}")
    else:
        print("Just what is it that you want?\nI'm confused")
