from itertools import combinations

def solution(relation):
    n, m = len(relation), len(relation[0])
    
    candidates = []
    for i in range(1, m + 1):
        candidates.extend(combinations(range(m), i))
    
    uniqueness = []
    for candi in candidates:
        temp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(temp)) == n:
            uniqueness.append(candi)
            
    answer = set(uniqueness)
    for i in range(len(uniqueness)):
        for j in range(i + 1, len(uniqueness)):
            if len(uniqueness[i]) == len(set(uniqueness[i]).intersection(set(uniqueness[j]))):
                answer.discard(uniqueness[j])
                
    return len(answer)
