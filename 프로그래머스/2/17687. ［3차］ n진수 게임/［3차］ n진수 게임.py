'''
    여러사람이 둥글게 앉아 숫자를 하나씩 차례대로 말하는 게임
    - 0부터 시작해서 차례대로 말함
    - 10 이상의 숫자부터는 한자리씩 끊어 말함
    
    n진법으로 바꿔서 게임할거임
    
    주인공의 순서: p
    미리 구할 주인공이 말할 숫자의 갯수: t
'''

def solution(n, t, m, p):
    def transform(number, key):
        result = ''
        check = '0123456789ABCDEF'
        
        while number > 0:
            number, mod = divmod(number, key)
            result += check[mod]

        return result[::-1]

    answer = ''
    total = '0'
    
    for i in range(1, m*t):
        total += transform(i, n)
        
    while len(answer) < t:
        answer += total[p-1]
        p += m
        
    return answer