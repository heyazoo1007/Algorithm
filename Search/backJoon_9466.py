import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

#[4,7,6]이 중복되게 세면 안되니까 visit 사용
#싸이클이 되는 경우는 방문한 숫자 중에 cycle에 있는 경우

def dfs(x):
    global result
    visit[x]=1
    cycle.append(x)
    if visit[data[x]]:        
        if data[x] in cycle:
            result+=cycle[cycle.index(data[x]):]
    else: 
        dfs(data[x])                

for _ in range(int(input())):
    n=int(input())
    data=list(map(int,input().split()))
    data=[0]+data
    visit=[1]+[0]*(n)
    result=[]
    for i in range(1,n+1):
        if not visit[i]:
            cycle=[]
            dfs(i)
  
    print(n-len(result))
