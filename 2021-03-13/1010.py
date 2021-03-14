import sys
import math

length = int(sys.stdin.readline())

def factorial(num):
    result = 1
    for i in range(1,num + 1):
        result *= i
    return result

for i in range(length):
    left,right = map(int, sys.stdin.readline().split())
    print(factorial(right) // factorial(left) // factorial(right - left))