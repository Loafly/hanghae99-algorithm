import math
#변수를 입력받는 방법
increase,decrease,v = input().split()

increase = int(increase)
decrease = int(decrease)
v = int(v)


result = math.ceil((v - increase) / (increase - decrease))

print(result + 1)