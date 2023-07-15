string = input()
target = input()
n = len(target)

stack = []

for i in range(len(string)):
    stack.append(string[i])
    if ''.join(stack[-n:]) == target:
        for _ in range(n):
            stack.pop()
            
if stack:
    print(''.join(stack))
else:
    print('FRULA')
