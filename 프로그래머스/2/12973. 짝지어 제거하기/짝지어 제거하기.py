def solution(s):
    """
    1. 동일한 알파벳이 두 개 붙어 있는 짝 찾기
    2. 빈 공간 이어 붙이기
    과정을 반복하여 모든 문자를 제거할 수 있다면 성공
    
    :param s: 문자열
    :return: 성공적으로 수행할 수 있다면 1, 이외에는 0
    """
    answer = -1
    stack = []
    
    for tmp_s in s:
        if len(stack) == 0:
            stack.append(tmp_s)
            continue
        
        if stack[-1] != tmp_s:
            stack.append(tmp_s)
            continue
            
        stack.pop()

    return int(len(stack) == 0)