import sys
input=sys.stdin.readline

n = int(input())
data=[[] for _  in range(n+1)]

for _ in range(n):
    result=list(map(int,input().split()))
    x=result.pop(0)
    result.pop(-1)
    for i in range(0,len(result),2):
        data[x].append([result[i],result[i+1]])
        data[result[i]].append([x,result[i+1]])
        
def dfs(x,weight):
    for i in data[x]:
        a,b=i
        if distance[a]==-1:
            distance[a]=b+weight
            dfs(a,b+weight)
            
distance=[-1]*(n+1)
distance[1]=0
dfs(1,0)

start=distance.index(max(distance))
distance=[-1]*(n+1)
distance[start]=0
dfs(start,0)

print(max(distance))
