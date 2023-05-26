n, k = map(int, input().split())
m = len(str(n))

visit = set()
visit.add((n, 0)) # 숫자, 연산횟수
queue = [[n, 0]]
answer = 0

while queue:
    number, times = queue.pop(0)
    
    if times == k:
        answer = max(answer, number) # 최대 숫자 업데이트
        continue
        
    number = list(str(number))
    for i in range(m - 1):
        for j in range(i + 1, m):
            if i == 0 and number[j] == '0':
                continue
            
            number[i], number[j] = number[j], number[i]
            temp = int(''.join(number))
            if (temp, times + 1) not in visit:
                queue.append([temp, times + 1])
                visit.add((temp, times + 1))
            # 배열 원상복구
            number[i], number[j] = number[j], number[i]
                
if answer == 0:
    print(-1)
else:
    print(answer)
