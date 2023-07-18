import heapq

n = int(input())
gifts = []

for _ in range(n):
    a = list(map(int, input().split()))
    
    if a[0] == 0:
        if len(gifts) == 0:
            print(-1)
            continue
        else:
            print(-1 * heapq.heappop(gifts))
            
    if a[0] != 0 :
        for i in range(1, len(a)):
            heapq.heappush(gifts, -a[i])
            
