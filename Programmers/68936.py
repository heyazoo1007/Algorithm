def solution(arr):
    answer = [0, 0]
    N = len(arr)
    
    def comp(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    m = n // 2
                    comp(x, y, m)
                    comp(x, y + m, m)
                    comp(x + m, y, m)
                    comp(x + m, y + m, m)
                    return
                
        #무사히 다 통과했다면 압축가능         
        answer[init] += 1
        
    comp(0, 0, N)
    
    return answer
