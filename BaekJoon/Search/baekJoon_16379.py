from collections import deque

n, t, g = map(int, input().split())

queue = deque() # 숫자, 횟수 
queue.append(n)
flag = False
visit = [0] * (10 ** 5 + 1)
visit[n] = 1
while queue:
    number = queue.popleft()
    
    if number == g:
        if visit[number] - 1 <= t:
            flag = True
            print(visit[number] - 1)
            break             
        
    for each in [number + 1, number * 2]:
        if 1 <= each <= 99999 :
            if each == number + 1:
                if not visit[each]:
                    queue.append(each)
                    visit[each] = visit[number] + 1
            elif each == number * 2:
                count = len(str(each))
                temp = each - 10 ** (count - 1)
                if not visit[temp]:
                    queue.append(temp)
                    visit[temp] = visit[number] + 1
        else:
            break
                
if flag == False:
    print('ANG')
