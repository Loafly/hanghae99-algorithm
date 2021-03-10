import sys
length = int(input())

virus = [False] * length
computer_list = []

for i in range(int(input())):
    computer_list.append(list(input().split()))

print(computer_list)