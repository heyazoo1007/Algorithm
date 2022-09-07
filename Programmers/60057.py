def solution(s):
    n = len(s)    
    answer = 1001
    for i in range(1, n + 1):
        temp = s[ : i]
        count = 1
        result = ''
        for j in range(i, n + i, i):
            if temp == s[j : j + i] :
                count += 1
            else:
                if count == 1:
                    result += temp
                else: 
                    result += (str(count) + temp)
                    count = 1                
                temp = s[j : j + i]      
        answer = min(answer, len(result))
        
    return answer
