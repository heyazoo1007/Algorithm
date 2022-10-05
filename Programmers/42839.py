import math
from itertools import permutations

def isPrime(num):
    flag = True
    if num == 1 or num == 0:
        return False
    
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
        
    if flag:
        return True
              
def solution(numbers):
    
    numbers = list(numbers)
    n = len(numbers)
    
    answer = 0
    check = []
    for i in range(1, n + 1):
        #순열로 i자리수 숫자를 임의 생성한다
        result = permutations(numbers, i)
        #만들어진 i자리수 수 중에서 소수이고, 중복이 안되는 경우를 센다 
        for x in result:
            temp = int(''.join(x))           
            if isPrime(temp) and temp not in check:
                answer += 1
                check.append(temp)
        
    return answer
