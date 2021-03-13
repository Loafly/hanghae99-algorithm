import sys

people = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split()))

min_time = sum(time_list)

while time_list:
    time_list.remove(max(time_list))
    min_time += sum(time_list)

print(min_time)


