import sys

def DFS(x,y):
    global count
    if f'{x},{y}' in check_dictionary:
        return count
    else:
        check_dictionary[f'{x},{y}'] = True
        if square_list[x][y] == 1:
            count += 1
            #위
            if y > 0:
                DFS(x,y - 1)
            #아래
            if y < length - 1:
                DFS(x,y + 1)
            #오른쪽
            if x < length - 1:
                DFS(x + 1, y)
            #왼쪽
            if x > 0:
                DFS(x - 1, y)
        
        return count

length = int(sys.stdin.readline())

square_list = []
count_list = []

check_dictionary = {
}

for i in range(length):
    string = sys.stdin.readline().rstrip('\n');
    temp_list = []
    for char in string:
        temp_list.append(int(char))
    square_list.append(temp_list)

for i in range(length):
    for j in range(length):
        count = 0
        count = DFS(i, j)
        if count > 0:
            count_list.append(count)

count_list.sort()
print(len(count_list))
for count in count_list:
    print(count)