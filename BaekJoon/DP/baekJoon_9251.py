x=list(input())
y=list(input())
n=len(x)
m=len(y)
dp=[[0]*n for _ in range(m)]

if x[0]==y[0]:
    dp[0][0]=1
else:
    dp[0][0]=0
    
for i in range(1,n):
    if x[i]==y[0]:
        dp[0][i]=1
    else: 
        dp[0][i]=dp[0][i-1]
        
for j in range(1,m):
    if y[j]==x[0]:
        dp[j][0]=1
    else:
        dp[j][0]=dp[j-1][0]

for i in range(1,m):
    for j in range(1,n):
        if y[i]==x[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
print(dp[-1][-1])
