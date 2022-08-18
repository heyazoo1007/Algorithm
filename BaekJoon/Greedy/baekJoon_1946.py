for _ in range(int(input())):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int,input().split())))
    zero = sorted(data,key=lambda x: x[0])
    #선발인원 수 
    count = 1
    result = zero[0][1]
    
    for i in range(1,n):
        if zero[i][1] < result:
            count += 1
            result = zero[i][1]     
            
    print(count)
