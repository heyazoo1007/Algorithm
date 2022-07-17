N,K=map(int,input().split())
data=list(input())
result=[]
k=K

for i in range(N):

    #뺄 수 있는 횟수가 남아있고, 더 큰 숫자가 오른쪽에 있고, 아직 가장 큰 숫자가 오지 않았을 때
    while k>0 and result and result[-1]<data[i]:
    
        #result의 오른쪽 원소를 제거해야하므로
        result.pop()
        k-=1
        
    result.append(data[i])
    
print(''.join(result[:N-K]))
