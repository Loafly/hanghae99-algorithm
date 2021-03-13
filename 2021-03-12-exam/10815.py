sanggeun_length = input()
sanggeun_card = list(map(int,input().split()))
sanggeun_card.sort()

check_length = input()
check_card = list(map(int,input().split()))

result_list = []

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False

for card in check_card:
    if is_existing_target_number_binary(card,sanggeun_card):
        result_list.append(1)
    else:
        result_list.append(0)

for i in range (0, len(result_list)):
    print(result_list[i], end = ' ')