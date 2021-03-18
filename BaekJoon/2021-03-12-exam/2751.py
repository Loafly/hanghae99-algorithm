import sys
length = int(sys.stdin.readline())

sort_result = []
num_input_list = []


def merge_sort(array):
    # 이 곳을 채워보세요!
    if len(array) == 1:
        return array
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])
    print('left_array = ',left_array)
    right_array = merge_sort(array[mid:])
    print('right_array = ', right_array)
    return merge(left_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1
    print('result = ', result)
    return result


for i in range(length):
    num_input_list.append(int(sys.stdin.readline()))

sort_result = merge_sort(num_input_list)

for element in sort_result:
    print(element)