# var_class = int(input())

# for i in range(0,var_class):
#     score = input().split()
#     total_score = 0
#     avg = 0
#     avg_over = 0

#     for j in range(0,int(score[0])):
#         total_score = total_score + int(score[j + 1])
    
#     avg = total_score / int(score[0])

#     for j in range(0,int(score[0])):
#         if int(score[j + 1]) > avg:
#             avg_over += 1    
    
#     result = avg_over / int(score[0]) * 100

#     print(str(result) + '%')



# while, for, if, 자료형, Index, input()



# a = input()
# list = []
# for x in a:
#     list.append(x)
# count = 0
# for x in list:
#     # print(x)
#     if x == 'c':
#         try:
#             index = list.index(x)
#             if list[index+1] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'c':
#         try:
#             index = list.index(x)
#             if list[index+1] == '-':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'd':
#         try:
#             index = list.index(x)
#             if list[index+1] == 'z' and list[index+2] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 list[index+2] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'd':
#         try:
#             index = list.index(x)
#             if list[index+1] == '-':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'l':
#         try:
#             index = list.index(x)
#             if list[index+1] == 'j':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'n':
#         try:
#             index = list.index(x)
#             if list[index+1] == 'j':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 's':
#         try:
#             index = list.index(x)
#             if list[index+1] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x == 'z':
#         try:
#             index = list.index(x)
#             if list[index+1] == '=':
#                 list[index] = 0
#                 list[index+1] = 0
#                 count += 1
#             else:
#                 list[index] = 0
#                 count += 1
#         except:
#             pass
#     elif x != 0:
#         index = list.index(x)
#         list[index] = 0
#         count += 1
#     else:
#         pass
#     # print(list)
#     # print(count)
# print(count)



# a = 5 

# if a % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# x % 5 
# a = 5

# 6 = 5 * 1  .... 1

# for i in range(0,100):
#     if i % a == 0:
#         print()


# import sys
# def hanoi(n, source, transfer, dest):
#     if n==1:
#         move.append([source, dest])
#     else:
#         hanoi(n-1,source, dest, transfer) <= 2개이상을 옮기는 경우
#         move.append([source, dest])
#         hanoi(n-1, transfer, source, dest)

# move =[]
# hanoi(int(sys.stdin.readline()),1,2,3)
# print(len(move))
# print('\n'.join([''.join(str(i) for i in row)for row in move]))