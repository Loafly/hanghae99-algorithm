#변수를 입력받는 방법
a = input()             
b = input()             

#문자를 숫자로
a = int(a)              

#b의 마지막 자리
b_first = int(b[0])     
b_second = int(b[1])    
b_third = int(b[2])     

first = a * b_first     
second = a * b_second   
third = a * b_third     

#출력
print(third)
print(second)
print(first)

print(a * int(b))