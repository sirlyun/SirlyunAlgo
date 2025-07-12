def solution(numbers):
    """
    제일 앞자리 숫자가 클 수록 유리
    30과 3의 경우 고려
    이어 붙이기

    :param numbers: 0 또는 양의 정수 리스트
    :return: 이어 붙여 만들 수 있는 가장 큰 숫자 (문자열로 변환)
    """

    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    for i in numbers:
        answer += i

    return str(int(answer))