length = int(input())
cur_value = 1

stack = []
queue = []
result = []
is_impossible = False
for i in range(length):
    queue.append(input())

#queue에 값이 없을때 까지
while queue:
    if not stack:
        stack.append(cur_value)
        result.append('+')
        cur_value += 1
    else:
        if int(stack[-1]) != int(queue[0]):
            stack.append(cur_value)
            result.append('+')
            cur_value += 1
        else:
            stack.pop()
            queue.pop(0)
            result.append('-')
    if cur_value > length + 1:
        is_impossible = True
        break

if is_impossible:
    print('NO')
else:
    for i in result:
        print(i)