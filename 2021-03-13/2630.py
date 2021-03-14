import sys
import math

square_length = int(sys.stdin.readline())

square_list = []
square_store = []

count_zero = 0
count_one = 0

for i in range(square_length):
    square_list.append(list(map(int, sys.stdin.readline().split())))

square_store.append(square_list)
# print(square_store)

is_zero = False
is_one = False
for row in square_list:
    if 1 in row:
        is_one = True
    if 0 in row:
        is_zero = True

if not is_zero:
    count_one += 1
    square_store.clear()
elif not is_one:
    count_zero += 1
    square_store.clear()

while square_store:    
    square = square_store.pop(0)
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
            #왼쪽 위
            temp_left_up_list.append(square[i][j])
            #오른쪽 위
            temp_rigth_up_list.append(square[i][j + half_size])
            #왼쪽 아래
            temp_left_down_list.append(square[i + half_size][j])
            #오른쪽 아래
            temp_right_down_list.append(square[i + half_size][j + half_size])
    
        square_left_up_list.append(temp_left_up_list)
        square_rigth_up_list.append(temp_rigth_up_list)
        square_left_down_list.append(temp_left_down_list)
        square_right_down_list.append(temp_right_down_list)

    #왼쪽 위
    is_zero = False
    is_one = False
    for row in square_left_up_list:
        if 1 in row:
            is_one = True
        if 0 in row:
            is_zero = True

    if is_one and is_zero:
        # print('square_left_up_list = ', square_left_up_list)
        square_store.append(square_left_up_list)
    elif not is_zero:
        count_one += 1
    else:
        count_zero += 1

    #오른쪽 위
    is_zero = False
    is_one = False
    for row in square_rigth_up_list:
        if 1 in row:
            is_one = True
        if 0 in row:
            is_zero = True

    if is_one and is_zero:
        # print('square_rigth_up_list = ', square_rigth_up_list)
        square_store.append(square_rigth_up_list)
    elif not is_zero:
        count_one += 1
    else:
        count_zero += 1

    #왼쪽 아래
    is_zero = False
    is_one = False
    for row in square_left_down_list:
        if 1 in row:
            is_one = True
        if 0 in row:
            is_zero = True

    if is_one and is_zero:
        # print('square_left_down_list = ', square_left_down_list)
        square_store.append(square_left_down_list)
    elif not is_zero:
        count_one += 1
    else:
        count_zero += 1

    #오른쪽 아래
    is_zero = False
    is_one = False
    for row in square_right_down_list:
        if 1 in row:
            is_one = True
        if 0 in row:
            is_zero = True

    if is_one and is_zero:
        # print('square_right_down_list = ', square_right_down_list)
        square_store.append(square_right_down_list)
    elif not is_zero:
        count_one += 1
    else:
        count_zero += 1

print(count_zero)
print(count_one)