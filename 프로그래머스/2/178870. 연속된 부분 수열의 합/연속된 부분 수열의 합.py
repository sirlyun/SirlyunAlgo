def solution(sequence, k):
    """
    조건
    기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
    부분 수열의 합은 k입니다.
        합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
            길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.
    :param sequence: 정수 수열
    :param k: 만들어야 하는 숫자 합
    :return: 조건에 맞는 부분 수열
    """
    n = len(sequence)
    left = 0
    current_sum = 0
    answer = [0, n]

    for right in range(n):
        current_sum += sequence[right]

        while current_sum > k and left <= right:
            current_sum -= sequence[left]
            left += 1
        
        if current_sum == k:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]

    return answer
