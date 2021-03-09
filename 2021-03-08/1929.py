import math

#변수를 입력받는 방법
min,max = input().split()
min_number = int(min)
max_number = int(max)

prime = []

for i in range(min_number, max_number + 1):
    prime_check = True
    #제곱근 구하기
    sqrt_number = int(math.sqrt(i + 1))
    for j in range(2, sqrt_number + 1):
        if i % j == 0:
            prime_check = False
            break
    if prime_check:
        prime.append(i)

if min_number == 1:
    prime.remove(1)
    
for i in range(0, len(prime)):
    print(prime[i])