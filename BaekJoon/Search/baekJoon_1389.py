from collections import deque

n,m= map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(v):
    num=[0]*(n+1)
    queue=deque()
    queue.append(v)
    visit[v]=1
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if not visit[i]:
                num[i]=num[x]+1
                queue.append(i)
                visit[i]=1
    return sum(num)
            

ans=[]
for i in range(1,n+1):
    visit=[0]*(n+1)
    ans.append(bfs(i)) #케빈 값들 넣는다
    
k=min(ans)
print((ans.index(k))+1)
