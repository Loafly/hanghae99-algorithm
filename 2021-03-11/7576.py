import sys

row, col = map(int, sys.stdin.readline().split())

tomato_store = []

for i in range(col):
   tomato = list(map(int, sys.stdin.readline().split()))
   tomato_store.append(tomato)


tomato_grow = []
for i in range(col):
    for j in range(row):
        if tomato_store[i][j] == 1:
            tomato_grow.append([i,j])


for i in range(len(tomato_grow)):
     print(tomato_grow[i][0], tomato_grow[i][1])
     row
