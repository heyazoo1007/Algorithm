n,k=map(int,input().split())
coins=[]
dp=[0]*(k+1)
dp[0]=1
for _ in range(n):
    coins.append(int(input()))

for i in coins:
    for j in range(1,k+1):
        if j>=i:
            dp[j]+=dp[j-i]
            
print(dp[k])
