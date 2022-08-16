def solution(id_list, report, k):  
    directory = {}
    banned = {}
    n = len(id_list)
    m = len(report)
    answer = [0]*n
    final = []
    
    for i in range(n):
        directory[id_list[i]] = []
        banned[id_list[i]] = []
        
    for i in range(m):
        a,b = report[i].split()   
        #a가 신고한 b
        if b not in directory[a]: 
            directory[a].append(b)
        #b를 신고한 a, 정지당하는 사람 세려고            
        if a not in banned[b]:
            banned[b].append(a)
                    
    for name in banned.keys():
        if len(banned[name]) >= k :
            final.append(name)
    k = 0        
    for i in directory.keys():
        count = 0        
        for j in final:
            if j in directory[i]:
                count += 1      
        answer[k] = count
        k += 1 
    return answer

