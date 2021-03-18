#변수를 입력받는 방법

char_list = [['[', ']'], ['(', ')']]

while True:
    text = input()
    stack = []
    if text == '.':
        break
    
    for char in text:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if len(stack) == 0:
                print('no')
                break
            if char == ')' and stack[-1] == '(' or char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
                

