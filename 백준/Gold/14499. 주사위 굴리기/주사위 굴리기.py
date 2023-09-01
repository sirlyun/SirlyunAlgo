'''
    크기가 NxM인 지도가 존재
    지도 위에 주사위 하나가 x, y에 있다
    지도의 좌표는 r, c로 표현
    처음에는 주사위 모든 면에 0이 적혀있다
    지도에 각 칸에는 숫자가 적혀있다
    주사위를 굴렸을 때 이동한 칸에 쓰여있는 숫자가 0이면 주사위의 바닥면에 쓰여있는 숫자가 지도에 복사된다
    0이 아닌 경우에는 반대로 지도에 있는 숫자가 주사위에 복사되고 지도는 0이 된다
    동서북남 1 2 3 4
'''

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

con = list(map(int, input().split()))

nx, ny = x, y
for i in con:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])