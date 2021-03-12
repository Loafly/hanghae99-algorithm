import sys
length = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

min_value = sequence[0]
value_raise = {
    
}

def fibo_dynamic_programming(n, value_raise):
    # 구현해보세요!
    if n in value_raise:
        return value_raise[n]

    nth_fibo = fibo_dynamic_programming(n-1, value_raise) + fibo_dynamic_programming(n-2, value_raise)
    value_raise[n] = nth_fibo
    return nth_fibo