def solution(n, words):
    m = len(words)
    passed = []
    i = 1
    count = 1
    flag = True
    while words : 
        if i == n + 1:
            i = 1
            count += 1
        x = words.pop(0)
        if x in passed:
            flag = False
            break
        elif len(passed) > 0:
            if passed[-1][-1] != x[0]:
                flag = False
                break
        passed.append(x)
        i += 1
    
    if not flag: 
        return [i, count]
    else: 
    	return [0,0]
