import heapq
import sys

point_count, line_count = sys.stdin.readline().split()

point_count = int(point_count)
line_count = int(line_count)

start_point = int(sys.stdin.readline())

line_dic = {}
for i in range(line_count):
    u, v, w = sys.stdin.readline().split()
    if int(u) in line_dic:
        line_dic[int(u)].append((int(v),int(w)))
    else:
        line_dic[int(u)] = [(int(v),int(w))]

    print(line_dic)


def dijkstra(graph, start):
    
    distances = {node: float('inf') for node in range(line_count)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
        print(f'distances = {distances}')
        for line in graph[current_node]:
            print(line)
            adjacent = line[0]            
            weight = line[1]
            distance = current_distance + weight
            
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
                
    return distances


print(dijkstra(line_dic, 1))