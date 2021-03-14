import sys
import collections
point, line, start_point = map(int, sys.stdin.readline().split())

graph = []

def BFS(start_point, graph, check):
    temp_list = []
    temp_list.append(start_point)
    # end_value = start_point
    while temp_list:
        cur_value = temp_list.pop(0)
        check[cur_value - 1] = True
        print(cur_value, end=' ')
        for i in range(line):
            left_value = graph[i][0]
            right_value = graph[i][1]

            if left_value == cur_value:
                if not check[right_value - 1] and right_value not in temp_list:
                    temp_list.append(right_value)

            elif right_value == cur_value:
                if not check[left_value - 1] and left_value not in temp_list:
                    temp_list.append(left_value)

        # if end_value == cur_value and temp_list:
        #     temp_list.sort()
        #     end_value = temp_list[-1]                    


def DFS(start_point, graph, check):
    if check[start_point - 1]:
        return 0
    else:
        print(start_point, end=' ')
        temp_list = []
        check[start_point - 1] = True
        
        for i in range(line):
            if graph[i][0] == start_point:
                temp_list.append(graph[i][1])
                # DFS(graph[i][1], graph, check)
            elif graph[i][1] == start_point:
                temp_list.append(graph[i][0])
                # DFS(graph[i][0], graph, check)
        
        # temp_list.sort()
        while temp_list:
            DFS(temp_list.pop(0), graph, check)


for i in range(line):
    graph.append(list(map(int, sys.stdin.readline().split())))

graph.sort()

check_list = [False] * point
DFS(start_point, graph, check_list)
print()

check_list = [False] * point
BFS(start_point, graph, check_list)
