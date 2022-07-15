n=int(input())
work=[]
ans=[0]*1000
for _ in range(n):
    work.append(list(map(int,input().split())))
    
work.sort(reverse = True, key = lambda x: x[1])    

for i in range(n):
    for j in range(work[i][0]-1,-1,-1):
        if ans[j]==0:
            ans[j]=work[i][1]
            break
print(sum(ans))
