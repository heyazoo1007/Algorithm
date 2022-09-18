def solution(str1, str2):
    #글자를 두개씩 쪼개기 
    str1 = str1.lower()
    str2 = str2.lower()
    
    one, two = [], []    
    for i in range(1, len(str1)):
        if 97 <= ord(str1[i - 1]) <= 122:
            if 97 <= ord(str1[i]) <= 122:
                one.append(str1[i - 1:  i + 1])
                
    for i in range(1, len(str2)):
        if 97 <= ord(str2[i - 1]) <= 122:
            if 97 <= ord(str2[i]) <= 122:
                two.append(str2[i - 1:  i + 1])

    if len(one) == 0 and len(two) == 0:       
        return 65536
    else:
        #교집합 원소 구하는데 약간 애 먹음
        intersection = []    
        union = len(one) + len(two)
        if len(one) < len(two):
            for i in range(len(one)):
                if one[i] in two:
                    intersection.append(one[i])
                    two.pop(two.index(one[i]))
        else:
            for i in range(len(two)):
                if two[i] in one:
                    intersection.append(two[i])
                    one.pop(one.index(two[i]))
                    
        union -= len(intersection)
        answer = int((len(intersection) / union) * 65536)
        
        return answer
