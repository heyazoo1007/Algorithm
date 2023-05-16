n = int(input())
cities_budget = sorted(list(map(int, input().split())))
budget = int(input())

result = 0
left, right = 0, cities_budget[-1]
while left <= right : # 등호 빼먹으면 틀림
    mid = (left + right) // 2

    total = 0
    for i in range(n):
        total += min(cities_budget[i], mid) # 간결하게 표현하기 
    
    if total > budget:
        right = mid - 1
    else:
        result = mid # mid로 예산을 분배할 수 있을 때 result에 할당
        left = mid + 1
        
answer = 0    
for city in cities_budget:
    answer = max(answer, min(result, city))
    
print(answer)
