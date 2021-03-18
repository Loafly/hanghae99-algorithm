import sys
import collections

def password_catch(string):
    string = string.rstrip('\n')
    left_list = []
    right_list = []
    result = []

    for char in string:        
        if char == '<':
            if left_list:
                right_list.append(left_list.pop())
        elif char == '>':
            if right_list:
                left_list.append(right_list.pop())
        elif char == '-':
            if left_list:
                left_list.pop()
        else:
            left_list.append(char)


    if left_list:
        for value in left_list:
            result.append(value)
    if right_list:
        right_list.reverse()
        for value in right_list:
            result.append(value)

    return result

length = int(sys.stdin.readline())

for i in range(length):
    string = sys.stdin.readline()
    
    result = password_catch(string)
    print(''.join(result[i] for i in range(len(result))))