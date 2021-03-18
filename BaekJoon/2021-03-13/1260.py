import sys
import collections
point, line, start_point = map(int, sys.stdin.readline().split())

graph = {

}

def BFS(start_point, graph, check):
    queue = collections.deque([start_point])
    while queue:
        cur_value = queue.popleft()
        if check[cur_value]:
            continue
        else:
            check[cur_value] = True
            for cur_line in graph[cur_value]:
                if not check[cur_line]:
                    queue.append(cur_line)
            print(cur_value, end= ' ')

def DFS(start_point, graph, check):

    if check[start_point]:
        return
    else:
        print(start_point, end=' ')
        check[start_point] = True
        for cur_line in graph[start_point]:
            if not check[cur_line]:
                DFS(cur_line, graph, check)

for i in range(point):
    graph[i + 1] = []

for i in range(line):
    start, end = map(int, sys.stdin.readline().split())
    if start in graph:
        graph[start].append(end)
        graph[end].append(start)

for array in graph:
    graph[array].sort()

check = [False] * (point + 1)
DFS(start_point, graph, check)
print()
check = [False] * (point + 1)
BFS(start_point, graph, check)