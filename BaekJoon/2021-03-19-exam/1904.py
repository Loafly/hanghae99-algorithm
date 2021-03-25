import sys
target_level = int(sys.stdin.readline())

memo = {
    1 : 1,
    2 : 2
}

for i in range(3, 1000001):
    
    memo[i] = memo[i - 1] + memo[i - 2]

    memo[i] = memo[i] % 15746

    if target_level == i:
        break

print(memo[target_level])
# def DP(add_value, cur_level, target_level, sequence_list):
#     if cur_level > target_level:
#         return
#     elif cur_level == target_level:
#         global count
#         count += 1
#         return
    
#     DP('00', cur_level + 2, target_level, sequence_list)
#     DP('1', cur_level + 1, target_level, sequence_list)
    
# count = 0
# sequence_list = []
# DP('00', 2, target_level, sequence_list)
# DP('1', 1, target_level, sequence_list)

# print(count)