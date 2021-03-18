import sys
length = int(input())

virus = [False] * length
computer_list = []

for i in range(int(input())):
    computer_list.append(list(map(int,input().split())))

def virus_connet_count(index):
    if virus[index] == True:
        return
    else:
        virus[index] = True
        for computer in computer_list:
            if computer[0] == index + 1:
                virus_connet_count(computer[1] - 1)
            elif computer[1] == index + 1:
                virus_connet_count(computer[0] - 1)


virus_connet_count(0)
print(virus.count(True) - 1)
