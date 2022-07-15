import sys
input=sys.stdin.readline

n,m=map(int,input().split())
j=int(input())
apples=[]
for _ in range(j):
    apples.append(int(input()))
answer=0
current=[1,m]
if m==1:
    for i in range(1,j):
        answer+=abs(apples[i]-apples[i-1])
    print(answer)
else:
    for i in range(j):
        if apples[i]>current[1]:
            answer+=(apples[i]-current[1])
            current[0]=apples[i]-(m-1)
            current[1]=apples[i]
        elif apples[i]<current[0]:
            answer+=(current[0]-apples[i])
            current[0]=apples[i]
            current[1]=apples[i]+(m-1)
    print(answer)
