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


def DFS(start_point, target_point, weight, weigth_list, check_list):
    if check_list[start_point]:
        return
    elif start_point == target_point:
        weigth_list.append(weight)
        return 
    else:
        check_list[start_point] = True
        if start_point in line_dict:
            cur_weight = weight
            for element in line_dict[start_point]:
                weight = cur_weight + element[1]
                DFS(element[0], target_point, weight, weigth_list, check_list)
            
for i in range(point_count):
    weight = 0
    weigth_list = []
    check_list = [False] * (point_count + 1)
    DFS(start_point, i + 1, weight, weigth_list, check_list)
    if weigth_list:
        print(min(weigth_list))
    else:
        print('INF')
    weigth_list.clear()