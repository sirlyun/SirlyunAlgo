def solution(A,B):
    """
    A와 B의 길이는 같다
    A, B에서 각각 한개의 숫자를 뽑아 곱한다
    배열의 길이만큼 반복하여 곱한 값을 누적한다
    :param A: 자연수로 이루어진 배열
    :param B: 자연수로 이루어진 배열
    :return: 누적값의 최소
    """
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer