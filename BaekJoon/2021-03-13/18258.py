import sys
import collections

length = int(sys.stdin.readline())
queue = collections.deque([])

def command(command_list):
    if len(command_list) == 1:        
        if command_list[0] == 'empty':
            return 0 if queue else 1
        if command_list[0] == 'size':
            return len(queue)
        if queue:       
            if command_list[0] == 'pop':
                return queue.popleft()
            if command_list[0] == 'back':
                return queue[-1]
            if command_list[0] == 'front':
                return queue[0]
        else:
            return -1
    elif len(command_list) == 2:
        if command_list[0] == 'push':
            queue.append(command_list[1])

for i in range(length):
    command_list = list(sys.stdin.readline().split())    
    result = command(command_list)
    if result is not None:
        print(result)