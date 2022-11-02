def solution(compressed):
    compressed = list(compressed)
    stack = []
    
    for i in range(len(compressed)):
        if compressed[i] == ')':
            result = ''
            number = 0
            while stack:
                x = stack.pop()
                if x == '(':
                    temp = []
                    for i in range(len(stack) - 1, -1, -1):
                        if stack[i].isdigit():
                            temp = [stack[i]] + temp
                            stack.pop()
                        else:
                            break
                    number = int(''.join(temp))
                    break
                else:
                    result = x + result     
                    
            for i in range(number):
                stack.append(result)
                        
        else:
            stack.append(compressed[i])
            
    return ''.join(stack)
