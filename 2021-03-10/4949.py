#변수를 입력받는 방법
while True:
    text = input()
    stack = []
    if text == '.':
        break
    
    for char in text:
        if char == '(' or char == ')' or char == '[' or char == ']':
            stack.append(char)
    
    for i in range(len(stack) // 2) :
        stack()
    print(stack)
