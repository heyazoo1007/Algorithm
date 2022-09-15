from collections import deque

n,m=map(int,input().split())
data=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    data[b].append(a)

def bfs(v):
    visit=[0]*(n+1)
    visit[v]=1
    queue=deque()
    queue.append(v)
    while queue:
        x=queue.popleft()
        for i in data[x]:
            if not visit[i]:
                visit[i]=1
                count[v]+=1
                queue.append(i)                   

count=[0]*(n+1)
result=0
for i in range(1,n+1):
    bfs(i)
    result=max(result,max(count))
    
for i in range(1,n+1):
    if count[i]==result:
        print(i, end = ' ')
