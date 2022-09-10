import sys
sys.setrecursionlimit(10**6)

n=int(input())
data=list(map(int,input().split()))
target=int(input())

def dfs(x,data):  
    data[x]=-2
    for i in range(n):
        if x==data[i]:
            dfs(i,data)
        
dfs(target,data)

count=0
for i in range(n):
    #삭제 되지 않은 자식 노드
    if data[i]!=-2 and (i not in data):
        count+=1
        
print(count)
