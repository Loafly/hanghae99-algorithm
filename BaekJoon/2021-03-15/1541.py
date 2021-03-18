import sys

origin_string = sys.stdin.readline()

split_string = list(origin_string.split('-'))

min_sum = 0
start_plus = True
if origin_string[0] == '-':
    start_plus = False

for i in range(len(split_string)):

    num_list = list(map(int, split_string[i].split('+')))

    if i == 0 and start_plus:
        min_sum += sum(num_list)    
    else:
        min_sum -= sum(num_list)

print(min_sum)