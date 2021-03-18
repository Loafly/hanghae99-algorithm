def solution(begin, target, words):
    answer = 0
    visited = {

    }

    result_list = []

    visited[begin] = False
    for i in range(len(words)):
        visited[words[i]] = False

    if target in words:
        DFS(begin, target, words, 0, visited, result_list)
        answer = min(result_list)
    
    print(answer)
    return answer


def DFS(cur_word, target_word, words, level, visited, result_list):
    if visited[cur_word]:
        return
    
    if cur_word == target_word:
        result_list.append(level)
        return 
    
    visited[cur_word] = True

    for i in range(len(words)):
        word = words[i]
        dif_count = 0
        del_word = ''
        for j in range(len(word)):
            if word[j] != cur_word[j]:
                dif_count += 1
                if dif_count > 1:
                    break
        
        if dif_count == 1:
            new_word = word
            del_word = words.pop(i)
            DFS(new_word, target_word, words, level + 1, visited, result_list)
        
            visited[cur_word] = False
            words.append(del_word)

solution('hit','cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])