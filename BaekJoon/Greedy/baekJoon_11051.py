import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    result = [0]*n
    result[-1] = data[-1]
    
    for i in range(n-2,-1,-1):
        if data[i] > data[i+1] and data[i] > result[i+1]:
            result[i] = data[i]
        else:
            result[i] = result[i+1]
            
    answer=0
    for i in range(n):
        answer += result[i]-data[i]
    print(answer)
