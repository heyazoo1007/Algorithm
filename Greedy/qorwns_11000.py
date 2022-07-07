import heapq

n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
data.sort()
last=[]
heapq.heappush(last, data[0][1])
for i in range(1,n):
    if data[i][0]< last[0]:
        heapq.heappush(last,data[i][1])
    else:
        heapq.heappop(last)
        heapq.heappush(last,data[i][1])
print(len(last))
