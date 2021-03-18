def solution(n, computers):
    answer = 0

    visited = [False] * n
    network_count = [0] * n

    for i in range(n):
        DFS(n, computers, i, visited, network_count)

    print(network_count)

    return answer


def DFS(n, computers, cur_row, visited, network_count):
    for i in computers[cur_row]:
        print(f'computers = {computers}')
        if computers[cur_row][i] == 1:
            if i != cur_row:
                
                computers[cur_row][i] = 0
                computers[i][cur_row] = 0
                DFS(n,computers,i, visited, network_count)
            
            network_count[i] = 1

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])

