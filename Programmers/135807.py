import math

def get_common(arr): #리스트의 모든 원소 약수를 모두 모아서 반환하는 함수 
    temp = []
    arr.sort()
    num = arr[-1]
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            temp.append(i)
            temp.append(num // i)
            
    result = []
    for i in range(len(temp)):
        flag = True
        for j in range(len(arr)):
            if arr[j] % temp[i] != 0:
                flag = False
                break
        if flag:
            result.append(temp[i])
            
    return result

def operation(arr, commons):
    answer = []
    for i in range(len(commons)):
            flag = True
            for j in range(len(arr)):
                if arr[j] % commons[i] == 0:
                    flag = False
                    break
            if flag:
                answer.append(commons[i])
    return answer
                         
def solution(arrayA, arrayB):
    if len(arrayA) == 1 and len(arrayB) == 1:
        min_num, max_num = min(arrayA[0], arrayB[0]), max(arrayA[0], arrayB[0])
        if max_num % min_num != 0: # 두 수는 소수 관계
            return max_num
    
    commons_A = get_common(arrayA) # A의 모든 원소를 나누는 공약수 
    commons_B = get_common(arrayB) # B의 모든 원소를 나누는 공약수 
    
    answer = []
    if len(commons_A) == 0 and len(commons_B) == 0:
        return 0
    
    elif len(commons_A) == 0:
        answer = operation(arrayA, commons_B)
        
    elif len(commons_B) == 0:
        answer = operation(arrayB, commons_A)
                
    else: 
        answer = operation(arrayA, commons_B)
        answer += operation(arrayB, commons_A)
                      
    if len(answer) == 0:
        return 0 
    else:
        return max(answer)
