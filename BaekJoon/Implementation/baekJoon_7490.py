import copy

def recursive(array, k):
    if len(array) == k:
        operator_list.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    recursive(array, k)
    array.pop()
    
    array.append('+')
    recursive(array, k)
    array.pop()
    
    array.append('-')
    recursive(array, k)
    array.pop()
    
    
t = int(input())
for _ in range(t):
    n = int(input())
    operator_list = []
    recursive([], n - 1)
    integer = [i for i in range(1, n + 1)]
    
    for operator in operator_list:
        string = ''
        for i in range(n - 1):
            string += str(integer[i]) + operator[i]     
        string += str(integer[-1])
        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()
