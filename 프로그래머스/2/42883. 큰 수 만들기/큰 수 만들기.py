def solution(number, k):
    """
    스택을 활용해 순서를 유지하면서, 큰수를 지속적으로 앞에 보내야 함
    마지막에 작은 수 k개 제거
    
    :param number: 문자열 형식으로 주어진 숫자
    :param k: 제거할 수의 개수
    :return: number에서 k개의 수를 제거했을 때 나올 수 있는 가장 큰 수
    """
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])