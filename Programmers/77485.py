def solution(rows, columns, queries):
    temp = [i for i in range(1, rows * columns + 1)]
    matrix = []
    index = 0
    for _ in range(rows):
        matrix.append(temp[index : index + columns])
        index += columns
         
    answer = []
    for query in queries:
        a1, a2, b1, b2 = query
        a1, a2, b1, b2 = a1 - 1, a2 - 1, b1 - 1, b2 - 1
        result = []
        n1, n2, n3, n4 = matrix[a1][b2], matrix[b1][b2], matrix[b1][b2], matrix[b1][a2]
        for i in range(b2, a2, -1):
            matrix[a1][i] = matrix[a1][i - 1]
            result.append(matrix[a1][i])

        for i in range(b1, a1, -1):
            if i == a1 + 1:
                matrix[i][b2] = n1
            else:
                matrix[i][b2] = matrix[i - 1][b2]
            result.append(matrix[i][b2])
                 
        for i in range(a2, b2):
            if i == b2 - 1:
                matrix[b1][i] = n3
            else:
                matrix[b1][i] = matrix[b1][i + 1]
            result.append(matrix[b1][i])
                
        for i in range(a1, b1):
            if i == b1 - 1:
                matrix[i][a2] = n4
            else:
                matrix[i][a2] = matrix[i + 1][a2]
            result.append(matrix[i][a2])
            
        answer.append(min(result))
            
            
    return answer
