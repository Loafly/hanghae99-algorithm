import sys
length = int(sys.stdin.readline())

def is_VPS(string):
    stack = []
    
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'NO'
            else:
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'


for i in range(length):
    string = sys.stdin.readline()
    print(is_VPS(string))