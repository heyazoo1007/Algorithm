n = int(input())
k = int(input())
data = list(map(int,input().split()))
data.sort()

distance = []
if k >= n:
    print(0)
else:
    for i in range(1,n):
        distance.append(data[i]-data[i-1])
    distance.sort(reverse=True)
    for _ in range(k-1):
        distance.pop(0)
        
    print(sum(distance))
