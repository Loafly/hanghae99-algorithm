#변수를 입력받는 방법
num = input()

count = 0

str_num = str(num)
init_num = str(num)
num_temp = ''
    
while True:
    if len(str_num) == 1:
        str_num = str(0) + str_num      

    num_temp = int(str_num[0]) + int(str_num[1])    

    if len(str(num_temp)) == 1:
        num_temp = str(0) + str(num_temp)

    str_num = str_num[1] + str(num_temp)[1]
    count += 1

    if int(init_num) == int(str_num):
        print(count)
        break