def solution(s):
    """
    스택 사용
    :param s: (와 )로 이루어진 문자열
    :return: 올바른 괄호인지 반환
    """
    answer = True
    check = []
    
    for c in s:
        if c == '(':
            check.append(c)
        
        else:
            if not check:
                return False
            check.pop()
            
    if check:
        return False
    
    return True