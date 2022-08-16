#정답풀이
n=int(input())   
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=i
    for j in range(1,i):
        if j**2>i:
            break
        dp[i]=min(dp[i],dp[i-j**2]+1)
print(dp[n])

#틀린 풀이
import math
n=int(input())
dp=[0]*(n+1)
flag=0
for i in range(1,n+1):
    if i%(math.sqrt(i))==0:
        dp[i]=1
        
for x in range(1,n+1):
    if dp[x]==1:
        flag=x
    dp[x]=dp[flag]+dp[x-flag]
print(dp[n])
