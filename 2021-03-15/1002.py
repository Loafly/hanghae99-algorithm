import sys
import math

length = int(sys.stdin.readline())

def able_to_exist_count(x1, x2, y1, y2, r1, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2)

    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1

    if distance > r1 + r2:
        return 0
    elif distance == r1 + r2:
        return 1
    elif distance < r1 + r2 and distance + min(r1, r2) == max(r1, r2):
        return 1
    elif distance < r1 + r2 and distance + min(r1, r2) > max(r1, r2):
        return 2
    else:
        return 0



for i in range(length):
    input_list = list(map(int, sys.stdin.readline().split()))
    
    x1 = input_list[0]
    x2 = input_list[3]

    y1 = input_list[1]
    y2 = input_list[4]

    r1 = input_list[2]
    r2 = input_list[5]

    print(able_to_exist_count(x1, x2, y1, y2, r1, r2))