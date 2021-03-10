length = int(input())

memo = {
    0 : [1, 0],
    1 : [0, 1]
}

def fibonacci(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    
    pre = fibonacci(n - 1, fibo_memo)
    pre_pre = fibonacci(n - 2, fibo_memo)
    nth_fibo = [pre[0] + pre_pre[0], pre[1] + pre_pre[1]]
    fibo_memo[n] = nth_fibo
    return nth_fibo

for i in range(length):
    count = []    
    result = fibonacci(int(input()),memo)
    print(result[0], result[1])