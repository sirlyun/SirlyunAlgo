'''
    사용 가능 연산
        x += n
        x *= 2
        x *= 3
'''

def solution(x, y, n):
    answer = 0
    check = set()
    check.add(x)
    
    while check:
        if y in check:
            return answer
        
        tmp_check = set()
        for i in check:
            if i+n <= y:
                tmp_check.add(i+n)

            if i*2 <= y:
                tmp_check.add(i*2)

            if i*3 <= y:
                tmp_check.add(i*3)
    
        check = tmp_check
        answer += 1
    
    return -1