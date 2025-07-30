def to_binary(num):
    cnt = 0

    while num > 0:
        num, mod = divmod(num, 2)
        if mod == 1:
            cnt += 1

    return cnt

def solution(n):
    """
    정의
        n보다 큰 자연수
        2진수로 변환했을 때 1의 개수가 동일한 수
        위 두 조건을 만족하는 수 중 가장 작은 수
    :param n: 자연수
    :return: 정의에 따른 n 다음 큰 숫자
    """
    answer = 0
    check_binary = to_binary(n)
    
    for tmp_n in range(n+1, 1000001):
        binary_n = to_binary(tmp_n)
        if binary_n == check_binary:
            answer = tmp_n
            break
    
    return answer