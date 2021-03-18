import sys

length = int(sys.stdin.readline())

stair_score = []

for _ in range(length):
    stair_score.append(int(sys.stdin.readline()))

memo = []
if len(stair_score) > 2:
    memo.append(stair_score[0])
    memo.append(stair_score[0] + stair_score[1])
    memo.append(max(stair_score[0] + stair_score[2], stair_score[1] + stair_score[2]))

    for i in range(3,length): 
        memo.append(max(memo[i-2] + stair_score[i] , memo[i-3] + stair_score[i] + stair_score[i - 1]))

if len(stair_score) == 0:
    print(-1)
elif len(stair_score) == 1:
    print(stair_score[0])
elif len(stair_score) == 2:
    print(stair_score[0] + stair_score[1])
else:
    print(memo[-1])