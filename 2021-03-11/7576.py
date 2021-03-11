import sys
import collections

tomato_store = collections.deque()
queue = collections.deque()

row, col = map(int, sys.stdin.readline().split())

for i in range(col):
   tomato = list(map(int, sys.stdin.readline().split()))
   tomato_store.append(tomato)


for i in range(col):
    for j in range(row):
        if tomato_store[i][j] == 1:
            queue.append([i,j])

max_date = 0

while queue:
    cur_index = queue.popleft()
    cur_row = cur_index[1]
    cur_col = cur_index[0]
    cur_value = tomato_store[cur_col][cur_row]

    #오른쪽
    if cur_row + 1 < row:
        if tomato_store[cur_col][cur_row + 1] == 0:
            tomato_store[cur_col][cur_row + 1] = cur_value + 1
            queue.append([cur_col,cur_row + 1])
    #왼쪽
    if cur_row - 1 > -1:
        if tomato_store[cur_col][cur_row - 1] == 0:
            tomato_store[cur_col][cur_row - 1] = cur_value + 1
            queue.append([cur_col,cur_row - 1])
    #위
    if cur_col - 1 > -1:
        if tomato_store[cur_col - 1][cur_row] == 0:
            tomato_store[cur_col - 1][cur_row] = cur_value + 1
            queue.append([cur_col - 1,cur_row])
    #아래
    if cur_col + 1 < col:
        if tomato_store[cur_col + 1][cur_row] == 0:
            tomato_store[cur_col + 1][cur_row] = cur_value + 1
            queue.append([cur_col + 1,cur_row])
    
    if cur_value > max_date:
        max_date = cur_value

is_0 = False
for i in range(col):
    for j in range(row):
        if tomato_store[i][j] == 0:
            is_0 = True
            break

if is_0:
    print(-1)
else:
    print(max_date - 1)