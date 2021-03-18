def solution(n, computers):
    answer = 0

    visited = [False] * n

    while False in visited:
        for i in range(len(visited)):
            if not visited[i]:
                DFS(n, computers, i, visited)
                answer += 1

    print(answer)

    return answer


def DFS(n, computers, cur_row, visited):

    if visited[cur_row]:
        return 

    visited[cur_row] = True
    for i in range(len(computers[cur_row])):
        # print(f'cur_row = {cur_row}')
        # print(f'computers[{cur_row}][{i}] = {computers[cur_row][i]}')
        # print(f'computers = {computers}')        
        if computers[cur_row][i] == 1:
            if i != cur_row:                
                computers[cur_row][i] = 0
                computers[i][cur_row] = 0
                DFS(n,computers,i, visited)

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])

