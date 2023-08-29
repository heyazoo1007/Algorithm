from collections import Counter
import sys
input = sys.stdin.readline #이거 해줘야 EOFError 발생 안함

n, score, minimum = map(int, input().split())

scores = list(map(int, input().split()))
scores.sort(reverse = True)

answer = -1
flag = True
if n <= minimum:
    if n < minimum:
        scores.append(score)
    elif n == minimum :
        if score > scores[-1]:
            scores.pop()
            scores.append(score)
        else:
            flag = False
    
    if flag : 
        temp = Counter(scores)
        result = sorted(temp.items(), key = lambda x : x[0], reverse = True)
        rank = 1
        for x, y in result:
            if x == score:
                answer = rank
                break
            rank += y
            
print(answer)
