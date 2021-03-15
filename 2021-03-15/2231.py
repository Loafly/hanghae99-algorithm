import sys
number = int(sys.stdin.readline())

cur_num = 0

while True:
    cur_num += 1
    temp_num = cur_num
    temp_num_sum = 0

    while temp_num != 0:
        temp_num_sum += temp_num % 10
        temp_num = temp_num // 10
        
    temp_num_sum += cur_num
    
    if temp_num_sum == number:
        print(cur_num)
        break
    elif cur_num > number:
        print(0)
        break
