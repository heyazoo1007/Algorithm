def solution(n):
    count = 0
    if n == 1:
        return 1
    
    if n % 2 == 0:
        n = n // 2               
    else:
        n -= 1
        count += 1
        
    while True:       
        if n == 1:
            count += 1
            break
        if n % 2 == 1:
            count += 1
            n-= 1
        else:
            n //= 2
            
    return count
