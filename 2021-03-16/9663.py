import sys

N = int(sys.stdin.readline())

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):    
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate, ):
    if current_row == N:
        global count
        count += 1
        return 
    
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate)
            current_candidate.pop()

count = 0
DFS(N, 0, [])
print(count)
