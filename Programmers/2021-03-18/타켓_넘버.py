def target_number(numbers, target, cur_index, sum_number, plus_minus):
    global answer
    if plus_minus == '+':
        sum_number += numbers[cur_index]
    else:
        sum_number -= numbers[cur_index]
    if cur_index == len(numbers) -1:
        if sum_number == target:
            answer += 1
        return
    else:
        target_number(numbers, target, cur_index + 1, sum_number, '+')
        target_number(numbers, target, cur_index + 1, sum_number, '-')   

def solution(numbers, target):
    global answer
    answer = 0
    cur_index = 0
    sum_number = 0

    target_number(numbers, target, cur_index, sum_number, '+')
    target_number(numbers, target, cur_index, sum_number, '-')
    
    return answer     


solution([1,1,1,1,1], 3)