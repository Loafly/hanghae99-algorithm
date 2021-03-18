import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

A_dic = {i:True for i in A}

for i in range(len(B)):
    if B[i] in A_dic:
        print(1)
    else:
        print(0)    