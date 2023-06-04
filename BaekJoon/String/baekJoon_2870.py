answer = []
for _ in range(int(input())):
    temp = '' # 그때그때마다 숫자들 모으는 용도
    word = list(input())
    for i in range(len(word)):
        if word[i].isdigit():
            temp += word[i]
        if not word[i].isdigit() or i == len(word) - 1:
            if temp != '':
                answer.append(int(temp))
                temp = '' 

answer.sort()
for i in range(len(answer)):
    print(answer[i])
