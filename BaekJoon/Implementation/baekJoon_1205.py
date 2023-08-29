from collections import Counter
import sys
input = sys.stdin.readline

n, score, minimum = map(int, input().split())

scores = list(map(int, input().split()))
scores.sort(reverse = True)

flag = True
answer = -1
 
if flag : 
    if n < minimum:
        scores.append(score)
        temp = Counter(scores)
        result = sorted(temp.items(), key = lambda x : x[0], reverse = True)
        rank = 1
        for x, y in result:
            if x == score:
                answer = rank
                break
            rank += y
            
    elif n == minimum : 
        if score > scores[-1]:
            scores.pop()
            scores.append(score)
            temp = Counter(scores)
            result = sorted(temp.items(), key = lambda x : x[0], reverse = True)
            rank = 1
            for x, y in result:
                if x == score:
                    answer = rank
                    break
                rank += y
        
print(answer)
   
