from itertools import combinations

n, m = map(int, input().split())

chicken = []
house = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            chicken.append([i, j])
        if temp[j] == 1:
            house.append([i, j])

answer = 1e9
candidates = list(combinations(chicken, m))
for candidate in candidates:
    count = 0
    for x, y in house:
        temp = 1e9
        for i, j in candidate:
            temp = min(temp, abs(x - i) + abs(y - j))
        count += temp
    answer = min(answer, count)
        
print(answer)
