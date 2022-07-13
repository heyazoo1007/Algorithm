n=int(input())
data=list(map(int,input().split()))
sequence=[0]*n

for i in range(n):
    j=i+1    
    while True:
        
        if j>=n:
            break
        if data[j]>=data[i]:
            break
        else:
            sequence[i]+=1
        j+=1
print(max(sequence))
