n=int(input())
dp=[0]*31
dp[0]=1
for i in range(2,n+1,2):
    dp[i]+=3*dp[i-2]
    for j in range(0,i-3,2): #0부터 n-4까지의 값은 2를 곱해서 더해준다
        dp[i]+=2*dp[j]
print(dp[n])
