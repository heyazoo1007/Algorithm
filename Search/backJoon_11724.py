import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
data=[[] for _ in range(n+1)]

for _ in range(m):
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
            dfs(i)
            
count=0  
visit=[0]*(n+1) 
for i in range(1,n+1):
    if not visit[i]:
        count+=1
        dfs(i)
        
