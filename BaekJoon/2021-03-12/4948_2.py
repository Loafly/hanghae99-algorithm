import math
import sys

while True:
    number = int(sys.stdin.readline())
    if number == 0:
        break
    min_number = number + 1
    max_number = number * 2

    prim_count = 0

    for i in range(min_number, max_number + 1):
        prime_check = True
        #제곱근 구하기
        sqrt_number = int(math.sqrt(i + 1))
        for j in range(2, sqrt_number + 1):
            if i % j == 0:
                prime_check = False
                break
        if prime_check:
            prim_count += 1

    print(prim_count)