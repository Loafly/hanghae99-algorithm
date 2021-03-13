import sys
coin_kinds, price = map(int, sys.stdin.readline().split())

coin_kinds_list = []
for i in range(coin_kinds):
    coin_kinds_list.append(int(sys.stdin.readline()))

coin_count = 0

for i in range(coin_kinds - 1, -1, -1):
    cur_coin = coin_kinds_list[i]
    if price >= cur_coin:
        cur_coin_count = price // cur_coin
        coin_count += cur_coin_count
        price = price - (cur_coin * cur_coin_count)

print(coin_count)