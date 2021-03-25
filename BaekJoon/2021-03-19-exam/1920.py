import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

# 딕셔너리를 이용한 풀이
# A_dic = {i:True for i in A}

# for i in range(len(B)):
#     if B[i] in A_dic:
#         print(1)
#     else:
#         print(0)    

# 이분탐색을 이용한 풀이
A.sort()

for i in range(len(B)):
    element = B[i]
    min = 0
    max = len(A) - 1
    mid = 0
    check = False

    while min <= max:
        mid = (min + max) // 2
        value = A[mid]
        
        if value > element:
            max = mid - 1
        elif value < element:
            min = mid + 1
        else:
            check = True
            break
    if check:
        print(1)
    else:
        print(0)    