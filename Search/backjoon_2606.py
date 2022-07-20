n=int(input())
m=int(input())
data=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
    data[a].sort()
    data[b].sort()
    
visit=[0]*(n+1)

def dfs(v):
    for i in data[v]:
        if not visit[i]:
            visit[i]=1
            dfs(i)
            
dfs(1)
print(sum(visit)-1)
