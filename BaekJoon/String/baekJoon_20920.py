import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

numbers = {} # [횟수, 길이]
for _ in range(n):
    word = input().rstrip()
    k = len(list(word))
    if  k >= m:
        if word in numbers.keys():
            numbers[word][0] += 1
        else:
            numbers[word] = [1, k]
            
result = sorted(numbers.items(), key = lambda x : (-x[1][0], -x[1][1], x[0]))
for i in range(len(result)):
    print(result[i][0])
