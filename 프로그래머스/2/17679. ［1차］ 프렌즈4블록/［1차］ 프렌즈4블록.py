def solution(m, n, board):
    """
    1. 2×2 형태로 4개가 붙어있을 경우 지우기
    2. 빈공간 채우기
    3. 다시 1번 (지울게 없으면 종료)

    :param m: 높이
    :param n: 폭
    :param board: 배치 정보
    :return: 지워지는 블록의 개수
    """
    answer = 0

    board = [list(x) for x in board]
    check = set()
    while True:
        # 2×2 형태로 4개가 붙어있을 경우 지우기
        for i in range(m-1):
            for j in range(n-1):
                now = board[i][j]
                if now is True:
                    continue
                
                if now == board[i+1][j] and now == board[i][j+1] and now == board[i+1][j+1]:
                    check.add((i, j))
                    check.add((i+1, j))
                    check.add((i, j+1))
                    check.add((i+1, j+1))

        # 지우기
        if check:
            answer += len(check)
            for c in check:
                board[c[0]][c[1]] = True
            check = set()
        else:
            break

        # 빈공간 채우기
        while True:
            flag = False
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] is not True and board[i+1][j] is True:
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        flag = True
            
            if flag is False:
                break
            
    return answer