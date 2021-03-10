import sys
length, element_count = map(int, sys.stdin.readline().split())

queue = []
target_queue = []
cur_index = 0
count = 0
for i in range(length):
    queue.append(i + 1)

target_queue = list(map(int, sys.stdin.readline().split()))

while target_queue:
    target_index = queue.index(target_queue[0])

    if target_index == cur_index:
        queue.pop(0)
        target_queue.pop(0)        
    else:
        if cur_index < target_index:
            rigth_move = target_index - cur_index
            left_move = -(len(queue) - (target_index - cur_index))
        else:
            rigth_move = len(queue) - (cur_index - target_index)
            left_move = target_index - cur_index
        
        if abs(rigth_move) <= abs(left_move):
            cur_index += rigth_move
            count += abs(rigth_move)
        else:
            cur_index += left_move
            count += abs(left_move)
        
        #계산한 index가 범위 밖일 경우
        if cur_index < 0:
            cur_index += len(queue)
        elif cur_index >= len(queue):
            cur_index -= len(queue)
        
        queue.pop(cur_index)
        target_queue.pop(0)
    
print(count)
