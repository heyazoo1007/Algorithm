n,m=map(int,input().split())
A,B = [], []
count=0
#행렬값들이 띄어쓰기 없이 나옴. split() 안 빼면 indexError 발생!
for _ in range(n):
    A.append(list(map(int,input())))
for _ in range(n):
    B.append(list(map(int,input())))             

def convert3x3(x,y,A):
    for i in range(x,x+3):
        for j in range(y,y+3):
             A[i][j]=1-A[i][j]
#convert3x3이 3단위라서 n-3이 제일 마지막이 되어야한다(n-3,n-2,n-1)
#안 그럼 인덱스 오류남              
for a in range(n-2):
    for b in range(m-2):
        if A[a][b] != B[a][b]:
            convert3x3(a,b,A)             
            count+=1
            
isTrue = False
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            isTrue=True
                                                
if isTrue:
    print(-1)
else:
    print(count)
