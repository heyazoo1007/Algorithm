n=int(input())
cranes=list(map(int,input().split()))
m=int(input())
boxes=list(map(int,input().split()))

cranes.sort(reverse=True)           
boxes.sort(reverse=True)
if cranes[0]<boxes[0]:
    print(-1)
else:
    answer=0
    while(len(boxes)>0):
        answer+=1
        for i in range(n):           
           for j in range(len(boxes)):
               if cranes[i]>=boxes[j]:
                   del boxes[j]
                   break
    print(answer)
