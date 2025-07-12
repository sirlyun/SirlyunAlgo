def solution(n):
    """
    방향 순서와 칸 이동을 고려하여 삼각형(리스트) 안에서 돌기 
    :param n: 높이 n, 넓이 n의 삼각형 
    :return: 달팽이 결과
    """
    triangle = [[0] * i for i in range(1, n+1)]
    go = [(1, 0), (0, 1), (-1, -1)]
    turn = 0
    y, x = 0, 0
    cnt = 1
    end_num = sum(i for i in range(1, n+1))

    while cnt <= end_num:
        triangle[y][x] = cnt
        cnt += 1
        dy, dx = go[turn]
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < n and triangle[ny][nx] == 0:
            y, x = ny, nx

        else:
            turn = (turn + 1) % 3
            dy, dx = go[turn]
            y += dy
            x += dx

    answer = []
    for row in triangle:
        for item in row:
            answer.append(item)
    return answer