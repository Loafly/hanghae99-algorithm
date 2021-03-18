import heapq
import sys

point_count, line_count = sys.stdin.readline().split()

point_count = int(point_count)
line_count = int(line_count)

start_point = int(sys.stdin.readline())

line_dic = {}

for i in range(point_count):
    line_dic[i + 1] = []

for i in range(line_count):
    u, v, w = sys.stdin.readline().split()
    line_dic[int(u)].append((int(v),int(w)))


def dijkstra(graph, start):
    distances = {node + 1: float('inf') for node in range(point_count)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue

        for line in graph[current_node]:
            adjacent = line[0]            
            weight = line[1]
            distance = current_distance + weight
    
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
             
    return distances

distance_dic = dijkstra(line_dic, start_point)

for value in distance_dic.values():
    if value == float('inf'):
        print('INF')
    else:
        print(value)