def score(arr, answers, x):
    i = 0
    for ans in answers:
        if i == len(arr):
            i = 0
        if ans == arr[i]:
            final[x] += 1
        i += 1
        
final = [0,0,0]                        
def solution(answers):
    answer = []
    global final
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    score(one, answers, 0)
    score(two, answers, 1)
    score(three, answers, 2)
               
    for i in range(1,4):
        if final[i - 1] == max(final):
            answer.append(i)
    answer.sort()
    
    return answer
