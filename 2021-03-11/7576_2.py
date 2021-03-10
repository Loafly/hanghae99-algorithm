import sys

row, col = map(int, sys.stdin.readline().split())

tomato_store = []
date_count = -1

for i in range(col):
   tomato = list(map(int, sys.stdin.readline().split()))
   tomato_store.append(tomato)


def check(check_list, i, j, arrow):
    if arrow == 'right':
        if j + 1  < len(check_list[i]):
            if check_list[i][j + 1] == 0:
                return True
            else:
                return False
        else:
            True


    elif arrow == 'left':
        if j - 1  > -1:
            if check_list[i][j - 1] == 0:
                return True
            else:
                return False
        else:
            True

    elif arrow == 'up':
        if i + 1  < len(check_list):
            if check_list[i + 1][j] == 0:
                return True
            else:
                return False
        else:
            True

    elif arrow == 'down':
        if i - 1  > -1:
            if check_list[i - 1][j] == 0:
                return True
            else:
                return False
        else:
            True

while True:
    tomato_grow = []
    date_count += 1
    for i in range(col):
        for j in range(row):
            if tomato_store[i][j] == 1 and (check(tomato_store, i,j,'right') or check(tomato_store, i,j,'left') or check(tomato_store, i,j,'up') or check(tomato_store, i,j,'down')):
                tomato_grow.append([i,j])

    for i in range(len(tomato_grow)):
        tomato_grow_row = tomato_grow[i][1]
        tomato_grow_col = tomato_grow[i][0]
    
        #오른쪽
        if tomato_grow_row + 1 < row:
            if tomato_store[tomato_grow_col][tomato_grow_row + 1] != -1:
                tomato_store[tomato_grow_col][tomato_grow_row + 1] = 1
        #왼쪽
        if tomato_grow_row - 1 > -1:
            if tomato_store[tomato_grow_col][tomato_grow_row - 1] != -1:
                tomato_store[tomato_grow_col][tomato_grow_row - 1] = 1
        #위
        if tomato_grow_col - 1 > -1:
            if tomato_store[tomato_grow_col - 1][tomato_grow_row] != -1:
                tomato_store[tomato_grow_col - 1][tomato_grow_row] = 1
        #아래
        if tomato_grow_col + 1 < col:
            if tomato_store[tomato_grow_col + 1][tomato_grow_row] != -1:
                tomato_store[tomato_grow_col + 1][tomato_grow_row] = 1 
    if not tomato_grow:
        break


is_0 = False
for i in range(col):
    for j in range(row):
        if tomato_store[i][j] == 0:
            is_0 = True
            break
if is_0:
    print(-1)
else:
    print(date_count)