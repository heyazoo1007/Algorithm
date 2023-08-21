from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    scores = list(map(int, input().split()))

    certified = Counter(scores)
    for x in certified.keys():
        if certified[x] < 6 : 
            certified[x] = -1
             
    result = {}   # {팀 번호 : [점수 배열]}
    score = 1
    for i in range(len(scores)):
        temp = scores[i]
        if certified[temp] != -1:
            if temp in result:
                result[temp].append(score)
            else:
                result[temp] = [score]
            score += 1

    answer = -1
    fifth = 0
    num_sum = 1e9
    for team, num_arr in result.items():
        if num_sum > sum(num_arr[:4]):
            answer = team
            fifth = num_arr[4]
            num_sum = sum(num_arr[:4])
        elif num_sum == sum(num_arr[:4]):
            if num_arr[4] < fifth:
                answer = team
                fifth = num_arr[4]
                num_sum = sum(num_arr[:4])
    print(answer)
