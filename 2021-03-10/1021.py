import sys
length, element_count = map(int, sys.stdin.readline().split())

queue = []
target_queue = []
for i in range(length):
    queue.append(i + 1)

target_queue = list(map(int, sys.stdin.readline().split()))

while True:
    for i in range(len(queue)):
        if queue[i] == target_queue[0]:
            queue.pop(i)
            

        


    
print(queue)
print(target_queue)
