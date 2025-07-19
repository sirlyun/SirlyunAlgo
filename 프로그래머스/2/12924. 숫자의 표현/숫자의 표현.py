from collections import deque

def solution(n):
    """
    :param n: 자연수 n
    :return: 연속된 자연수들로 n을 표현하는 방법의 수
    """
    answer = 0
    for num1 in range(1, n+1):
        check = 0
        for num2 in range(num1, n+1):
            check += num2
            if check == n:
                answer += 1
                break
            if check > n:
                break
        
    return answer