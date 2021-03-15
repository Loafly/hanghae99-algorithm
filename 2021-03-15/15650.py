import itertools
import sys
N, M = map(int,sys.stdin.readline().split())

N_list = []
for i in range(N):
    N_list.append(str(i + 1))

for i in list(map(' '.join, itertools.permutations(N_list, M))):
    print(i)