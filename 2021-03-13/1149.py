import sys

length = int(sys.stdin.readline())

RGB_price_list = []

for i in range(length):
    RGB_price_list.append(list(map(int, sys.stdin.readline().split())))

def bfs(i):
    for j in range(len(RGB_price_list[i])):
        if RGB_price_list[i - 1][(j + 1) % 3] < RGB_price_list[i - 1][(j + 2) % 3]:
            RGB_price_list[i][j] = RGB_price_list[i - 1][(j + 1) % 3] + RGB_price_list[i][j]
        else:
            RGB_price_list[i][j] = RGB_price_list[i - 1][(j + 2) % 3] + RGB_price_list[i][j]                 

for i in range(1, length):
    bfs(i)

print(min(RGB_price_list[length - 1]))