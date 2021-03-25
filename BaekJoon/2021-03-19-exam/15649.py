import itertools
import sys
N, M = map(int,sys.stdin.readline().split())

# itertools를 이용한 풀이
# N_list = []
# for i in range(N):
#     N_list.append(str(i + 1))

# for i in list(map(' '.join, itertools.permutations(N_list, M))):
#     print(i)


# 백트래킹을 이용한 풀이
def DFS(cur_value, cur_level, target_level, visited_list, result_list):
    if visited_list[cur_value]:
        return
    elif cur_level == target_level:
        for i in range(len(result_list)):
            print(result_list[i], end= ' ')
        print()
        return
    else:
        visited_list[cur_value] = True
        for i in range(1, N + 1):
            if not visited_list[i] and cur_value != i:
                result_list.append(i)
                DFS(i, cur_level + 1, target_level, visited_list, result_list)
                result_list.pop()

        visited_list[cur_value] = False                


result_list = []
visited_list = [False] * (N + 1)
DFS(0, 0, M, visited_list, result_list)