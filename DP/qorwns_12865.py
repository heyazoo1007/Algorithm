n,k=map(int,input().split())
weight=[0]
value=[0]
for _ in range(n):
    a,b=map(int,input().split())
    weight.append(a)
    value.append(b)
    
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1): #i가 현재 물건
    for j in range(1,k+1): #j가 현재의 무게
        if j >= weight[i]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][k])
