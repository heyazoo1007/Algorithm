n = int(input())
first = list(map(int, input().split()))
grow_term = list(map(int, input().split()))

result = []
for i in range(len(first)):
    result.append([first[i], grow_term[i]])
    
result.sort(key = lambda x : x[1])
    
answer = 0    
for i in range(len(result)):
    answer += i * result[i][1] + result[i][0]
    
print(answer)
