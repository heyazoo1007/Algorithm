def solution(files):
    
    result = []
    head, number, tail = '', '', ''
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[: i]
                number = file[i:]
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j : ]
                        number = number[: j]
                        break
                result.append([head, number, tail])
                head, number, tail = '', '', ''
                break
                      
    result = sorted(result, key = lambda x : (x[0].lower(), int(x[1])))
    
    answer = []
    for x in result:
        answer.append(x[0] + x[1] + x[2])
        
    return answer
