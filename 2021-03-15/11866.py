import sys
N, K = map(int,sys.stdin.readline().split())

player_list = []
for i in range(N):
    player_list.append(i + 1)

cur_index = 0

print('<', end='')
while True:
    cur_index = (cur_index + K - 1) % len(player_list)
    print(player_list.pop(cur_index), end= '')
    if not player_list:
        break
    print(', ',end='')
print('>')