import sys

length, max_sum = sys.stdin.readline().split()
cards = list(map(int,sys.stdin.readline().split()))

length = int(length)
max_sum = int(max_sum)

max_sum_three = 0

for i in range(length - 2):
    for j in range(i + 1, length - 1, 1):
        for k in range(j + 1, length, 1):
            temp_sum = cards[i] + cards[j] + cards[k]
            if temp_sum >= max_sum_three and temp_sum <= max_sum:
                max_sum_three = temp_sum
            
        
print(max_sum_three)