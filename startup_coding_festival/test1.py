# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# import sys

# def solution(length, K):
#     min = 0
#     max = length
#     mid = 0

#     while min <= max:
#         mid = (min + max) // 2
#         count = (K * mid) - mid
        
#         if count > length:
#             max = mid - 1
#         else:
#             min = mid + 1
    
#     return max

# length, K = map(int, sys.stdin.readline().split())

# sequence = sys.stdin.readline()

# print(solution(length,K))




# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# import sys

# length, K = map(int, sys.stdin.readline().split())

# sequence = sys.stdin.readline()

# if K != length:
# 	print(length // K + length % K + (length // K // K))

# else:
# 	print(1)

import sys

length, K = map(int, sys.stdin.readline().split())

sequence = sys.stdin.readline().split()

count = 0

for i in range(K):
        if sequence:
            sequence.pop()

count += 1

while sequence:
    for i in range(K - 1):
        if sequence:
            sequence.pop()
    
    count += 1

print(count)