n = int(input())
k = int(input())

def get_num_smaller(x):
    num_smaller = 0
    for i in range(1, n + 1):
        num_smaller += min(n, (x - 1) // i)
        
    return num_smaller

def get_num_bigger(x):
    num_bigger = 0
    for i in range(1, n + 1):
        num_bigger += n - min(n, x // i)
        
    return num_bigger

low, high = 1, min(n * n , int(1e9))
answer = -1 
while low <= high:
    mid = (low + high) // 2
    
    num_smaller = get_num_smaller(mid)
    num_bigger = get_num_bigger(mid)
    
    if num_smaller > k - 1:
        high = mid - 1
    elif num_bigger > n * n - k:
        low = mid + 1
    else:
        answer = mid 
        break
        
print(answer)
