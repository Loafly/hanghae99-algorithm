import sys

length = int(sys.stdin.readline())

stair_score = []

for _ in range(length):
    stair_score.append(int(sys.stdin.readline()))

dp = []
if len(stair_score) > 2:
    dp.append(stair_score[0])
    dp.append(stair_score[0] + stair_score[1])
    dp.append(max(stair_score[0] + stair_score[2], stair_score[1] + stair_score[2]))

    for i in range(3,length): 
        dp.append(max(dp[i-2] + stair_score[i] , dp[i-3] + stair_score[i] + stair_score[i - 1]))

if len(stair_score) == 0:
    print(-1)
elif len(stair_score) == 1:
    print(stair_score[0])
elif len(stair_score) == 2:
    print(stair_score[0] + stair_score[1])
else:
    print(dp[-1])