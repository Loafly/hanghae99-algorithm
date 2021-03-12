import sys
length = int(sys.stdin.readline())

memo = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 2,
    5 : 2
}

def triangle_length(n, memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = triangle_length(n -1,memo) + triangle_length(n - 5,memo)        
        return memo[n]

for i in range(length):
    step = int(sys.stdin.readline())
    print(triangle_length(step,memo))
    