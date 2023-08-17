import sys
input = sys.stdin.readline

arr = set()
for _ in range(int(input())):
    temp = input().split()
    if len(temp) == 2:
        command, number = temp[0], temp[1]
        number = int(number)
    else:
        command = temp[0]
    
    if command == 'add':
        arr.add(number)
        
    if command == 'remove':
        if number in arr:
            arr.remove(number)
            
    if command == 'check':
        if number in arr:
            print(1)
        else:
            print(0)
            
    if command == 'toggle':
        if number in arr:
            arr.remove(number)
        else:
            arr.add(number)
    if command == 'all':
        
        arr = set([i for i in range(1, 21)])
        
    if command == 'empty':
        arr = set()
