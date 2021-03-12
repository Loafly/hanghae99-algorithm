import collections

length = int(input())

card_list = collections.deque([i for i in range(1,length + 1)])

count = 1

while len(card_list) != 1:
    temp = card_list.popleft()
    if count % 2 == 0:
        card_list.append(temp)

    count += 1

print(card_list[0])