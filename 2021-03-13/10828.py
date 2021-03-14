import sys

length = int(sys.stdin.readline())
stack = []

def command(command_list):
    if len(command_list) == 1:        
        if command_list[0] == 'empty':
            return 0 if stack else 1
        if command_list[0] == 'size':
            return len(stack)
        if stack:       
            if command_list[0] == 'pop':
                return stack.pop()
            if command_list[0] == 'top':
                return stack[-1]
        else:
            return -1
    elif len(command_list) == 2:
        if command_list[0] == 'push':
            stack.append(command_list[1])

for i in range(length):
    command_list = list(sys.stdin.readline().split())    
    result = command(command_list)
    if result is not None:
        print(result)