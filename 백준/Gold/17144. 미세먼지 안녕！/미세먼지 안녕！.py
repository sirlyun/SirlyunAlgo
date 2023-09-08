'''
    공기청정기는 항상 1번 열에 설치되어 있고 크기는 두행을 차지
    공기청정기가 설치안된 칸에는 미세먼지가 있고 그 칸에는 미세먼지 양이 들어있따
    1초동안 일어나는 일
        1. 미세먼지가 확산된다, 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다
            미세먼지가 있는 칸에서 인접한 방향으로 확산 BFS?
            인접한 방향에 공기청정기가 있거나 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
            확산되는 양은 그 칸에있는 미세먼지//5 이다.
            확산 원인 칸에 남아있는 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
        2. 공기청정기가 작동한다.
            위쪽 공기청정기의 바람은 반시계 순회, 아래쪽 공기청정기의 바람은 시계 순회
            바람이 불면 미세먼지가 바람 방향대로 한 칸씩 이동
            공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''

import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
dust_list = []

for r in range(R):
    if board[r][0] == -1:
        cleaner.append(r)
        cleaner.append(r+1)
        break
    

for t in range(T):
    tmp_list = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and board[i][j] != -1:
                tmp = 0
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    di = i+dx
                    dj = j+dy
                    if 0 <=di< R and 0<=dj<C:
                        if board[di][dj] != -1:
                            tmp_list[di][dj] += board[i][j] // 5
                            tmp += board[i][j] // 5
                board[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            board[i][j] += tmp_list[i][j]

    
    up_x, up_y = cleaner[0], 1
    down_x, down_y = cleaner[1], 1

    up_dx = [0, -1, 0, 1]
    up_dy = [1, 0, -1, 0]
    up_control = 0
    up_before = 0
    while True:
        di = up_x+up_dx[up_control]
        dj = up_y+up_dy[up_control]
        if up_x == cleaner[0] and up_y == 0:
            break
        if 0<=di<R and 0<=dj<C:
            board[up_x][up_y], up_before = up_before, board[up_x][up_y]
            up_x = di
            up_y = dj 
        else:
            up_control = (up_control+1)%4
    
    down_dx = [0, 1, 0, -1]
    down_dy = [1, 0, -1, 0]
    down_control = 0
    down_before = 0
    while True:
        di = down_x+down_dx[down_control]
        dj = down_y+down_dy[down_control]
        if down_x == cleaner[1] and down_y == 0:
            break
        if 0<=di<R and 0<=dj<C:
            board[down_x][down_y], down_before = down_before, board[down_x][down_y]
            down_x = di
            down_y = dj 
        else:
            down_control = (down_control+1)%4

result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            result += board[i][j]
print(result)