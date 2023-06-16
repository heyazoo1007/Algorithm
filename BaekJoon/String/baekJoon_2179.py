n = int(input())
a = [input() for _ in range(n)]

b = sorted(list(enumerate(a)), key = lambda x : x[1])

def check(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            count += 1
        else:
            break
    return count

length = [0] * (n + 1)
max_length = 0

for i in range(n - 1):
    temp = check(b[i][1], b[i + 1][1])
    max_length = max(max_length, temp)
    
    length[b[i][0]] = max(length[b[i][0]], temp)
    length[b[i + 1][0]] = max(length[b[i + 1][0]], temp)
    
first = 0
for i in range(n):
    if first == 0:
        if length[i] == max(length):
            first = a[i]
            print(first)
            pre = a[i][:max_length]
    else:
        if length[i] == max(length) and a[i][:max_length] == pre:
            print(a[i])
            break
