import math
import sys
length = int(sys.stdin.readline())

for i in range(length):
    date_conut = 0
    x, y = sys.stdin.readline().split()
    x = int(x)
    y = int(y)
    distance = y - x
    if distance <= 3:
        print(distance)
    else:        
        square_root = int(math.sqrt(distance))
        
        if distance == square_root ** 2:
            date_conut = 2 * square_root - 1
        elif distance > square_root ** 2  and distance <= square_root ** 2 + square_root:
            date_conut = 2 * square_root
        elif distance > square_root **2 + square_root:
            date_conut = 2 * square_root + 1    
        print(date_conut)