def solution(board, moves):
    n = len(board)
    basket = [-1]
    count = 0
    
    for col in moves: #움직이는 열 
        row = 0
        col -= 1
        flag = False
        for row in range(n):
            if board[row][col] != 0:
                flag = True
                break   
        if not flag:
            continue        
        elif board[row][col] != basket[-1] :
            basket.append(board[row][col])
            board[row][col] = 0
        elif board[row][col] == basket[-1]:
            basket.pop()
            count += 2
            board[row][col] = 0
        
        
    return count
