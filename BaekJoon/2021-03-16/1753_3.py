import sys
import collections
sys.setrecursionlimit(10**6)
point_count, line_count = sys.stdin.readline().split()
start_point = int(sys.stdin.readline())

point_count = int(point_count)
line_count = int(line_count)

line_dict = {    

}

for i in range(line_count):
    u,v,w = sys.stdin.readline().split()

    u = int(u)
    v = int(v)
    w = int(w)
    
    if u in line_dict:
        line_dict[u].append((v, w))
    else:
        line_dict[u] = [(v, w)]

def BFS(start_point, target_point, weight, weigth_list, check_list):
    
    queue = collections.deque()
    queue.append([start_point, 0])
    while queue:
        cur_value = queue.popleft()
        if cur_value[0] == target_point:
            return print(cur_value[1])

        if check_list[cur_value[0]]:
            continue 
        check_list[cur_value[0]] = True

        if cur_value[0] in line_dict:
            for element in line_dict[cur_value[0]]:
                weight = cur_value[1] + element[1]
                queue.append([element[0], weight])
    print('INF')
            
for i in range(point_count):
    weight = 0
    weigth_list = []
    check_list = [False] * (point_count + 1)
    BFS(start_point, i + 1, weight, weigth_list, check_list)