import sys
import collections

case_number = int(sys.stdin.readline())

for i in range(case_number):

    print_count, target_index = sys.stdin.readline().split()

    print_count = int(print_count)
    target_index = int(target_index)

    print_list = collections.deque(list(map(int, sys.stdin.readline().split())))

    for i in range(len(print_list)):
        print_list[i] = [print_list[i], i]


    count = 0
    cur_index = -1
    while True:
        if cur_index == target_index:
            break
        count += 1
        max_value = 0
        move_index = 0

        for i in range(len(print_list)):
            if max_value < print_list[i][0]:
                max_value = print_list[i][0]
                move_index = i

        print_list.rotate(-move_index)
        cur_node = print_list.popleft()
        cur_index = cur_node[1]        

    print(count)

