import sys

length = int(sys.stdin.readline())

stair_score = []

sum_score = 0

for i in range(length):
    stair_score.append(int(sys.stdin.readline()))

for i in range(3):
    stair_score.append(0)
cur_index = 0
while True:    
    sum_score += stair_score[cur_index]
    
    if cur_index >= length - 1:
        break
    if stair_score[cur_index + 1] > stair_score[cur_index + 2]:
        cur_index += 1
    elif stair_score[cur_index + 1] < stair_score[cur_index + 2]:
        cur_index += 2
    else:
        if stair_score[cur_index + 1] > stair_score[cur_index + 3]:
            cur_index += 1
        else:
            cur_index += 2    
    print(sum_score)

print(sum_score)

