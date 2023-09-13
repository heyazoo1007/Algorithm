h, w = map(int, input().split())
buildings = list(map(int, input().split()))

answer = 0
for i in range(1, w - 1):
    left_max = max(buildings[:i])
    right_max = max(buildings[i + 1:])
    
    compare = min(left_max, right_max)
    
    if buildings[i] < compare:
        answer += compare - buildings[i]
        
print(answer)
