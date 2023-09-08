import sys
input = sys.stdin.readline

players, member = map(int, input().split())

answer = [] # 방이 생성되어서 들어감 (인덱스 -> 방 번호), [인원수, 기준 레벨, [레벨, 닉네임]]
for i in range(players):
    level, nickname = input().split()
    level = int(level)
    flag = False
    
    for j in range(len(answer)):
        if answer[j][0] < member: 
            if answer[j][1] - 10 <= level <= answer[j][1] + 10:
                answer[j].append([level, nickname])
                answer[j][0] += 1
                flag = True
                break
    if not flag: # 기존에 있는 방에 못 들어감
        answer.append([1, level, [level, nickname]])
        
for i in range(len(answer)):
    if answer[i][0] == member :
        print('Started!')
        result = sorted(answer[i][2:], key = lambda x : x[1])
        for j in range(member):
            print(result[j][0], result[j][1])
    else: 
        print('Waiting!')
        result = sorted(answer[i][2:], key = lambda x : x[1])
        for j in range(answer[i][0]):
            print(result[j][0], result[j][1])
            
