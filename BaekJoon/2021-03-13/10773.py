import sys
length = int(sys.stdin.readline())

stack = []

for i in range(length):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))