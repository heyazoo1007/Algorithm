import sys

n = int(input())
people = []
answer = ''
for _ in range(n):
    people.append(list(map(int, input().split())))
    
for i in range(n):
    count = 0
    weight, height = people[i][0], people[i][1]
    for j in range(n):
        if people[j][0] > weight and people[j][1] > height:
            count += 1
            
    answer += str(count + 1) + ' '
    
print(answer)
