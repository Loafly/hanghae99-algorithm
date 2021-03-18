def solution(tickets):
    answer = []
    visited_dic = {

    }
    
    for i in range(len(tickets)):
        visited_dic[f'{tickets[i][0]}, {tickets[i][1]}'] = False

    visited_dic[f'0, 0'] = False

    print(visited_dic)

    sorted_tickets = sorted(tickets,key=lambda tickets: tickets[1])
    
    # DFS(sorted_tickets, answer, visited_dic, tickets[0][0], tickets[0][1])
    DFS(sorted_tickets, answer, visited_dic, '0', '0')

    return answer


def DFS(tickets, result, visited_dic, src, dest):    
    if visited_dic[f'{src}, {dest}']:
        visited_dic[f'{src}, {dest}'] = False
        return
    
    else:
        visited_dic[f'{src}, {dest}'] = True





solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
