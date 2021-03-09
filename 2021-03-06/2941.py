#변수를 입력받는 방법
text = input()
exception_text = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in range(0, len(exception_text)):
    text = text.replace(exception_text[i],"0")

print(len(text))