import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
data=[[] for _ in range(n+1)]
root=[0]*(n+1)
visit=[0]*(n+1)
visit[0]=1
visit[1]=1
for _ in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
    data[a].sort()
    data[b].sort()
    
def dfs(v):
    visit[v]=1
    for i in data[v]:
        if not visit[i]:
            visit[i]=1
            root[i]=v
            dfs(i)
 
dfs(1)
for i in range(2,n+1):
    print(root[i])
