n=int(input())
data=list(map(int,input().split()))
dp1=[0]*n
dp2=[0]*n
dp3=[0]*n
for i in range(n):
    for j in range(0,i+1):
        if data[i]>data[j] and dp1[i]<dp1[j]:
            dp1[i]=dp1[j]
    dp1[i]+=1
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if data[i]>data[j]and dp2[i]<dp2[j]:
            dp2[i]=dp2[j]
    dp2[i]+=1
    
for i in range(n):
    dp3[i]=dp1[i]+dp2[i]-1
print(max(dp3))
