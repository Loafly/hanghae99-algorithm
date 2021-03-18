import sys
import math
#변수를 입력받는 방법
tree_count, want_tree = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

def binary_search(target, array):
    min_value = 0
    mid_value = 0
    max_value = max(tree)

    while min_value <= max_value:
        mid_value = (min_value + max_value) //2
        rest = 0
        for i in array:
            if i >= mid_value:
                rest += i - mid_value
        
        if rest >= want_tree:
            min_value = mid_value + 1
            
        else:
            max_value = mid_value - 1
            
    return max_value

print(binary_search(want_tree,tree))