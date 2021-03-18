import sys
length = int(sys.stdin.readline())

group_count = 0

def is_group_word(string):
    is_exist = []
    for index in range(len(string)):
        if string[index] in is_exist:
            if string[index - 1] != string[index]:
                return False
        else:
            is_exist.append(string[index])
    return True

for i in range(length):
    string = sys.stdin.readline()
    if is_group_word(string):
        group_count += 1

print(group_count)