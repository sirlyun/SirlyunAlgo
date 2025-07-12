def quad(arr, x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 압축 불가능한 경우 쪼개기
            if arr[i][j] != arr[x][y]:
                n //= 2
                quad(arr, x, y, n)
                quad(arr, x+n, y, n)
                quad(arr, x, y+n, n)
                quad(arr, x+n, y+n, n)
                return
            
    answer[arr[x][y]] += 1
    return

def solution(arr):
    """
    압축 방법
        당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
        만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
        그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.

    :param arr: 0과 1로 이루어진 2^n x 2^n 크기의 2차원 정수 배열
    :return: 배열에 최종적으로 남는 0의 개수와 1의 개수를 담은 배열
    """
    global answer
    answer = [0, 0]
    quad(arr, 0, 0, len(arr))
    
    return answer