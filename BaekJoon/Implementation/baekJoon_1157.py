from collections import Counter

word = Counter(input().upper())

result = sorted(word.items(), key = lambda x : x[1], reverse = True)

count = 0
max_num = result[0][1]
answer = result[0][0]
for x, y in result:
    if y == max_num:
        count += 1

if count >= 2:
    print('?')
elif count == 1:
    print(answer)
    
