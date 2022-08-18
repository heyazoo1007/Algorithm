n = int(input())
distance = list(map(int,input().split()))
oil = list(map(int,input().split())) 

final = oil[0]
result = 0

for i in range(n-1):
    if oil[i] < final:
        final = oil[i]
    result += distance[i]*final
       	
print(result)
