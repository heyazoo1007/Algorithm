import heapq

n,k = map(int,input().split())
jewel,bag = [], []
for _ in range(n):
    jewel.append(list(map(int,input().split())))
    
for _ in range(k):
    bag.append(int(input()))
    
jewel.sort()
bag.sort()

count=0
answer=[]
for i in bag:
    #하나의 가방에 담을 수 있는 보석 후보 모두 저장
    while jewel and i >= jewel[0][0]:
        heapq.heappush(answer,-jewel[0][1])
        heapq.heappop(jewel)
    #보석 후보가 있다면 그 중에서 가장 작은 가격(-최대가격)을 넣는다 
    if answer:
        count+=heapq.heappop(answer)
print(-count)
