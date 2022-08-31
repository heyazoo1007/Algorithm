def solution(dartResult):
    answer = []
    index = 0
    score_idx = -1
    
    while index < len(dartResult):
        if dartResult[index].isdigit():
            end_index = index
            #두 자리 수가 있는 경우에 대비해서
            while dartResult[end_index].isdigit():
                end_index += 1
            if dartResult[end_index] == 'S':
                answer.append(int(dartResult[index:end_index]))
            elif dartResult[end_index] == 'D':
                answer.append(int(dartResult[index:end_index]) ** 2)
            elif dartResult[end_index] == 'T':
                answer.append(int(dartResult[index:end_index]) ** 3)
                
            score_idx += 1
            index = end_index + 1
            
        else:
            if dartResult[index] == '*':
                if score_idx == 0 :
                    answer[score_idx] *= 2
                else:
                    answer[score_idx - 1] *= 2
                    answer[score_idx] *= 2
            elif dartResult[index] == '#':
                answer[score_idx] *= -1
                
            index += 1
            
    return sum(answer)
