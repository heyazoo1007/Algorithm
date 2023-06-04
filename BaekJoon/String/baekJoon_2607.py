import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
first = input()
first_length = len(first)
dic = Counter(first) # 첫 번째 단어 구성

answer = 0
for _ in range(n - 1):
    name = input()
    length = len(name)
    temp = Counter(name)
    
    if first_length > length + 1 or first_length < length - 1:
        continue
    
    temp.subtract(dic)
    zero, one, minus_one = 0, 0, 0
    flag = True
    for each in temp.keys():
        # 다 0으로 이루어져 있거나, 나머지 0이고, 1이나 -1이 하나만 있으면 정답
        if temp[each] == 0:
            zero += 1
        elif temp[each] == 1:
            one += 1
        elif temp[each] == -1:
            minus_one += 1
        else:
            flag = False
            break
            
    if one + minus_one > 2:
        flag = False
    if one > 2 or minus_one > 2:
        flag = False
        
    if flag :
        answer += 1
print(answer)
