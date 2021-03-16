import sys

length = int(sys.stdin.readline())

sequence_list = list(map(int, sys.stdin.readline().split()))

asc_list = [0] * length
desc_list = [0] * length

for i in range(length):
    for j in range(i):
        if (sequence_list[i] > sequence_list[j] and asc_list[i] < asc_list[j]):
             asc_list[i] = asc_list[j]
    asc_list[i] += 1 

for i in range(length - 1, -1, -1):
    for j in range(length - 1, i, -1):
        if (sequence_list[i] > sequence_list[j] and desc_list[i] < desc_list[j]):
             desc_list[i] = desc_list[j]
    desc_list[i] += 1 

max_count = 0
for i in range(length):
    max_count = max(max_count,asc_list[i] + desc_list[i])

print(max_count - 1)