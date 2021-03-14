import math
import sys

length = int(sys.stdin.readline())

value_dictionary = {

}

value_list = []

for i in range(length):
    value = int(sys.stdin.readline())
    if value in value_dictionary:
        value_dictionary[value] += 1
    else:
        value_dictionary[value] = 1
    value_list.append(value)
    

sum_number = 0
max_frequency_list = []
max_frequency = 0

for number in value_dictionary:
    #덧셈 구하기
    sum_number += number * value_dictionary[number]
    
    #최빈값 구하기
    if max_frequency < value_dictionary[number]:
        max_frequency_list.clear()
        max_frequency = value_dictionary[number]
        max_frequency_list.append(number)

    elif max_frequency == value_dictionary[number]:
        max_frequency_list.append(number)
        
value_list.sort()
max_frequency_list.sort()

#산술평균
print(round(sum_number / length))
#중앙값
print(value_list[len(value_list) // 2])
#최빈값
if len(max_frequency_list) == 1:
    print(max_frequency_list[0])
else:
    print(max_frequency_list[1])
#최소, 최대 범위
print(value_list[-1] - value_list[0])

