import sys

length = int(sys.stdin.readline())

triangle_list = []

for i in range(length):
    triangle_list.append(list(map(int, sys.stdin.readline().split())))
    

def bfs(i):
    if i == 0:
        return triangle_list[0][0]
    for j in range(len(triangle_list[i])):
        
        if 0 < j < len(triangle_list[i]) - 1:
            rigth_up = triangle_list[i][j] + triangle_list[i - 1][j]
            left_up = triangle_list[i][j] + triangle_list[i - 1][j - 1]

            if left_up > rigth_up:
                triangle_list[i][j] = left_up
            else:
                triangle_list[i][j] = rigth_up

        elif j == 0:
            rigth_up = triangle_list[i][j] + triangle_list[i - 1][j]
            triangle_list[i][j] = rigth_up

        elif j == len(triangle_list[i]) - 1:
            left_up = triangle_list[i][j] + triangle_list[i - 1][j - 1]
            triangle_list[i][j] = left_up
            

for i in range(length):
    bfs(i)

print(max(triangle_list[length - 1]))