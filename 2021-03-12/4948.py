import sys
import math

prime = []

for i in range(2, (123456 * 2) + 1):
    prime_check = True
    #제곱근 구하기
    sqrt_number = int(math.sqrt(i + 1))
    for j in range(2, sqrt_number + 1):
        if i % j == 0:
            prime_check = False
            break
    if prime_check:
        prime.append(i)

while True:
    number = int(sys.stdin.readline())
    count = 0
    if number == 0:
        break

    for element in prime:
        if element > number:
            if element <= number * 2:
                count += 1
            else:
                break
    
    print(count)