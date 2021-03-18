import sys
length = int(sys.stdin.readline())
sequence_list = list(map(int, sys.stdin.readline().split()))

value_raise = [0] * length

for i in range(length):
    for j in range(i):
        if (sequence_list[i] > sequence_list[j] and value_raise[i] < value_raise[j]):
             value_raise[i] = value_raise[j]
    value_raise[i] += 1

print(max(value_raise))