def solution(msg):
    alphabet = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #사전에 있는 문자까지 진행하고, 그 단어의 인덱스 answer에 추가, 없는 문자열에서 멈추고 사전에 등록     
    answer = []
    msg = list(msg)
    now = msg.pop(0)
   
    while msg:
        nx = msg.pop(0)       
        current = now + nx
        if current not in alphabet:
            alphabet.append(current)
            answer.append(alphabet.index(now))
            now = nx             
        else: # current in alphabet
            now = current
            
    #마지막 남은 문자는 반복문에서 연산되지 않으므로 따로 해당 문자의 인덱스를 answer에 추가해준다
    if now != 0:
        answer.append(alphabet.index(now))
        
    return answer
