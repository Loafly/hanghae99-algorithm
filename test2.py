# var_class = int(input())

# for i in range(0,var_class):
#     score = input().split()
#     total_score = 0
#     avg = 0
#     avg_over = 0

#     for j in range(0,int(score[0])):
#         total_score = total_score + int(score[j + 1])
    
#     avg = total_score / int(score[0])

#     for j in range(0,int(score[0])):
#         if int(score[j + 1]) > avg:
#             avg_over += 1    
    
#     result = avg_over / int(score[0]) * 100

#     print(str(result) + '%')



# while, for, if, 자료형, Index, input()



# a = input()
# list = []
# for x in a:
#     list.append(x)
# count = 0
# for x in list:
#     # print(x)
#     if x == 'c':
#         try:
#             index = list.index(x)
#             if list[index+1] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'c':
#         try:
#             index = list.index(x)
#             if list[index+1] == '-':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'd':
#         try:
#             index = list.index(x)
#             if list[index+1] == 'z' and list[index+2] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 list[index+2] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'd':
#         try:
#             index = list.index(x)
#             if list[index+1] == '-':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'l':
#         try:
#             index = list.index(x)
#             if list[index+1] == 'j':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'n':
#         try:
#             index = list.index(x)
#             if list[index+1] == 'j':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 's':
#         try:
#             index = list.index(x)
#             if list[index+1] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'z':
#         try:
#             index = list.index(x)
#             if list[index+1] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x != 0:
#         index = list.index(x)
#         list[index] = 0
#         count += 1
#     else:
#         pass
#     # print(list)
#     # print(count)
# print(count)



# a = 5 

# if a % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# x % 5 
# a = 5

# 6 = 5 * 1  .... 1

# for i in range(0,100):
#     if i % a == 0:
#         print()


# import sys
# def hanoi(n, source, transfer, dest):
#     if n==1:
#         move.append([source, dest])
#     else:
#         hanoi(n-1,source, dest, transfer) <= 2개이상을 옮기는 경우
#         move.append([source, dest])
#         hanoi(n-1, transfer, source, dest)

# move =[]
# hanoi(int(sys.stdin.readline()),1,2,3)
# print(len(move))
# print('\n'.join([''.join(str(i) for i in row)for row in move]))

# prices = list(map(int, input().split()))
# op = []
# # 1 2 3 2 3
# # 4 3 1 1 0
# # 다 비교해야함
# while True:
#     counter = -1
#
#     if not prices:
#         break
#
#     for i in prices:
#         if prices[0] <= i:
#             counter += 1
#     op.append(counter)
#     prices.pop(0)
#
# print(op)
#
# memo = ['a']
#
# memo_ = {
#     'a' : 100
# }
#
# if 'a' in memo:
#     print('a')
#
# if 'a' in memo_:
#     print(memo_['a'])


# N, M, V
# N: 정점의 개수
# M: 간선의 개수
# V: 탐색 시작하는 번호

# import sys
# from collections import deque
# N, M, V = map(int, sys.stdin.readline().split())
# #print(N, M, V)
# dic = {}
# for i in range(N):
#     dic[i+1] = []
# #print(dic)
# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     dic[a].append(b)
#     dic[b].append(a)
# #print(dic)
#
# # DFS -> Stack
# def dfs(graph, start):
#     stack = [start]
#     visited = []
#     not_visited = []
#     is_found = False
#     while stack:
#         cur_node = stack.pop()
#         visited.append(cur_node)
#         print(graph)
#         print(f'graph[cur_node] = {graph[cur_node]}')
#         if len(graph[cur_node]) > 1:
#             for value in graph[cur_node]:
#                 if value not in visited :
#                     not_visited.append(value)
#                     is_found = True
#                     print('test1')
#             if is_found == True :
#                 stack.append(min(not_visited))
#                 not_visited = []
#                 is_found = False
#                 print('test2')
#             else:
#                 continue
#         else:
#             stack.append(graph[cur_node])
#             print('test3')
#     return visited
# print(dfs(dic, V))

# import sys
# from collections import deque
# N, M, V = map(int, sys.stdin.readline().split())
# #print(N, M, V)
# dic = {}
# for i in range(N):
#     dic[i+1] = []
# #print(dic)
# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     dic[a].append(b)
#     dic[b].append(a)
# #print(dic)
#
# # DFS -> Stack
# def dfs(graph, start):
#     stack = [start]
#     visited = []
#     not_visited = []
#     is_found = False
#     while stack:
#         cur_node = stack.pop()
#         visited.append(cur_node)
#         # if len(graph[cur_node]) > 1:
#         for value in graph[cur_node]:
#             if value not in visited :
#                 not_visited.append(value)
#                 is_found = True
#         if is_found == True :
#             stack.append(min(not_visited))
#             not_visited = []
#             is_found = False
#         else:
#             continue
#         # else:
#         #     stack.append(graph[cur_node])
#         #     print('test3')
#     return visited
# print(dfs(dic, V))

# from collections import deque

# deque = deque()

# deque.append('a')
# print(deque)                #deque(['a'])

# deque.appendleft('b')
# print(deque)                #deque(['b', 'a'])

# temp_deque = deque.copy()
# print(temp_deque)           #deque(['b', 'a'])

# deque.clear()
# print(deque)                #deque([])

# deque.extend(temp_deque)
# print(deque)                #deque(['b', 'a'])

# deque.append('c')
# print(deque)                #deque(['b', 'a', 'c'])

# deque.extendleft(temp_deque)
# print(deque)                #deque(['a', 'b', 'b', 'a', 'c'])

# print(deque.index('b'))     #1

# deque.insert(3,'d')
# print(deque)                #deque(['a', 'b', 'b', 'd', 'a', 'c'])

# print(deque.pop())          #c
# print(deque)                #deque(['a', 'b', 'b', 'd', 'a'])

# print(deque.popleft())      #a
# print(deque)                #deque(['b', 'b', 'd', 'a'])

# deque.remove('d')           #deque(['b', 'b', 'a'])
# print(deque)

# deque.reverse()             #deque(['a', 'b', 'b'])
# print(deque)

# deque.rotate(1)             #deque(['b', 'a', 'b'])
# print(deque)


dic = {
    'a' : 0,
    'b' : 1
}

print(dic)
print(dic[dic.keys[0]])