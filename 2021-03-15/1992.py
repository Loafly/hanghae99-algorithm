import sys
import math

square_length = int(sys.stdin.readline())

square_list = []
square_store = []

def DFS(square_arrow_list):
    square = square_arrow_list
    half_size = len(square) // 2

    square_left_up_list = []
    square_rigth_up_list = []
    square_left_down_list = []
    square_right_down_list = []

    for i in range(half_size):
        temp_left_up_list = []
        temp_rigth_up_list = []
        temp_left_down_list = []
        temp_right_down_list = []

        for j in range(half_size):
            # 왼쪽 위
            temp_left_up_list.append(square[i][j])
            # 오른쪽 위
            temp_rigth_up_list.append(square[i][j + half_size])
            # 왼쪽 아래
            temp_left_down_list.append(square[i + half_size][j])
            # 오른쪽 아래
            temp_right_down_list.append(square[i + half_size][j + half_size])

        square_left_up_list.append(temp_left_up_list)
        square_rigth_up_list.append(temp_rigth_up_list)
        square_left_down_list.append(temp_left_down_list)
        square_right_down_list.append(temp_right_down_list)

    print('(', end='')
    is_zero_one(square_store, square_left_up_list)
    is_zero_one(square_store, square_rigth_up_list)
    is_zero_one(square_store, square_left_down_list)
    is_zero_one(square_store, square_right_down_list)
    print(')', end='')


def is_zero_one(square_store, square_arrow_list):
    is_zero = False
    is_one = False
    for row in square_arrow_list:
        if not is_one or not is_zero:
            if 1 in row:
                is_one = True
            if 0 in row:
                is_zero = True
        else:
            break

    if is_one and is_zero:
        DFS(square_arrow_list)
        square_store.append(square_arrow_list)
    elif not is_zero:
        print(1, end='')
    else:
        print(0, end='')

for i in range(square_length):
    string = sys.stdin.readline().rstrip('\n');
    temp_list = []
    for char in string:
        temp_list.append(int(char))
    square_list.append(temp_list)

is_zero_one(square_store, square_list)

