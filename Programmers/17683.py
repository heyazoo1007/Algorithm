def getMusicArr(melody, time):
    temp = []
    for c in melody:
        if c == '#':
            temp[-1] += '#'
        else:
            temp.append(c)  
        
    if time == 0:
        return temp
            
    if time // len(temp) == 0:
        temp = temp[:time]
    else:
        temp = temp * (time // len(temp)) + temp[: time % len(temp)]
            
    return temp 

def checkSubArray(sub, arr):
    length = len(sub)
    for i in range(len(arr)):
        if sub == arr[i : i + length]:
            return True
    return False
    
def solution(m, musicinfos):
    answer = "(None)"
    answerTime = 0
    
    musics = []
    for i in range(len(musicinfos)):
        start, end, title, melody = musicinfos[i].split(',')
        
        s1, s2 = int(start[0 : 2]), int(start[3 : 5])
        e1, e2 = int(end[0 : 2]), int(end[3 : 5])
        hour, minute = e1 - s1, e2 - s2
        time = hour * 60 + minute
                       
        musicArr = getMusicArr(melody, time)
        m = getMusicArr(m, 0)
    
        if checkSubArray(m, musicArr):
            if answerTime < time:
                answer = title
                answerTime = time
    return answer
