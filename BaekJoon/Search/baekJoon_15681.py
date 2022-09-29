import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline #이걸 설정해줘야 시간초과 발생하지 않는다 

n,r,q = map(int,input().split())
data = [[] for _ in range(n+1)]
dp = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split()) 
    data[a].append(b)
    data[b].append(a)

def dfs(node):
    dp[node] = 1
    for i in data[node]:
        if not dp[i]:
            dfs(i)
            #잎노드에서부터 하나씩 추가해 가야하므로
            #dfs 후에 dp값을 누적해간다 
            dp[node] += dp[i]  
        
dfs(r)
for _ in range(q):   
    print(dp[int(input())])
