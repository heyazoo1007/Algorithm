t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    students=[]
    for _ in range(m):
        students.append(list(map(int,input().split())))
    students.sort()
    students.sort(key=lambda x: x[1])
    result=0
    count=[0]+[1]*n
    
    for i in range(m):
        a,b=students.pop(0)
        for j in range(a,b+1):
            if count[j]==1:
                count[j]=0
                result+=1
                break
                
    print(result)
