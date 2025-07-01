from itertools import product

def solution(word):
    answer = 0
    
    tmp = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(5):
        for check in product(tmp, repeat=i+1):
            result.append(''.join(check))
            
    answer = sorted(result).index(word) + 1
    return answer

