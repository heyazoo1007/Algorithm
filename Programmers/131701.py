def solution(elements):
    answer = elements
    sequence = elements + elements
    total = sum(elements)
    answer.append(total)
    n = len(sequence)
    
    for length in range(2, n):
        count = 0
        for i in range(n - length + 1):
            count = sum(sequence[i : i + length])
            if count > total:
                break            
            answer.append(count)
                
    return len(set(answer))
