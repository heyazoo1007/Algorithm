def solution(numbers):
    answer = []
    
    for number in numbers:
        bin_number = list('0' + bin(number)[2 : ])
        index = ''.join(bin_number).rfind('0') #가장 오른쪽에 있는 0의 인덱스
        bin_number[index] = '1'
        
        if number % 2 == 1:
            bin_number[index + 1] = '0'
        
        #2진수를 10진수로 변환해서 추가
        answer.append(int(''.join(bin_number), 2))
        
    return answer
