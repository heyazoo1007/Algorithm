import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = {}
total = n
for _ in range(n):
    word = input().rstrip()
    words[word] = 1
    
for _ in range(m):
    temp = list(input().rstrip().split(','))
    for each in temp:
        if each in words.keys():
            if words[each] > 0:
                total -= 1
                words[each] = 0
                    
    print(total)
