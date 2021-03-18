import sys
import collections

def password_catch(string):
    string = string.rstrip('\n')
    cur_index = 0
    result = collections.deque()
    for char in string:        
        if char == '<':
            if cur_index > 0:
                cur_index -= 1
        elif char == '>':
            if cur_index < len(result):
                cur_index += 1
        elif char == '-':
            if result:
                if cur_index > 0:
                    del result[cur_index - 1]
                    cur_index -= 1
        else:
            result.insert(cur_index,char)
            cur_index += 1
    return result

length = int(sys.stdin.readline())

for i in range(length):
    string = sys.stdin.readline()
    
    result = password_catch(string)
    print(''.join(result[i] for i in range(len(result))))