'''
    방은 NxM 크기
    방 안 각각의 칸은 벽 또는 빈 칸으로 구성
    청소기는 동서남북 중 한 방향을 바라봄
    방의 각 칸은 좌표 r, c로 표현
    청소기 작동 방식
        현재 칸이 청소되지 않은 경우 현재 칸 청소
        1.현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는경우
            방향 유지한체 한칸 후진 가능하면 한칸 후진하고 청소 체크
            후진 불가능하면 작동을 멈춘다
        2.현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는경우
            반시계 방향으로 방향 90도 회전
            바라보는 방향 기준으로 앞쪽 칸이 청소되지 않은 빈 칸이면 한칸 전진
            청소 체크
'''

N, M = map(int, input().split())
robot_r, robot_c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

clean_room = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
flag = False

while True:
    if flag:
        break
    # 현재 위치 청소 체크
    if room[robot_r][robot_c] == 0:
        clean_room += 1
        room[robot_r][robot_c] = 2
    # 주변 체크
    chk = 0
    for k in range(4):
        di = robot_r + dx[k]
        dj = robot_c + dy[k]
        if 0<=di<N and 0<=dj<M:
            if room[di][dj] == 0:
                chk += 1
    # 1의 경우
    if chk == 0:
        if d == 0:
            if 0<=robot_r+1<N:
                if room[robot_r+1][robot_c] != 1:
                    robot_r += 1
                else:
                    flag = True
            else:
                flag = True
        elif d == 1:
            if 0<=robot_c-1<M:
                if room[robot_r][robot_c-1] != 1:
                    robot_c -= 1
                else:
                    flag = True
            else:
                flag = True
        elif d == 2:
            if 0<=robot_r-1<N:
                if room[robot_r-1][robot_c] != 1:
                    robot_r -= 1
                else:
                    flag = True
            else:
                flag = True
        else:
            if 0<=robot_c+1<M:
                if room[robot_r][robot_c+1] != 1:
                    robot_c += 1
                else:
                    flag = True
            else:
                flag = True
    # 2의 경우
    else:
        if d == 0:
            d = 3
            if 0<=robot_c-1<M:
                if room[robot_r][robot_c-1] == 0:
                    robot_c -= 1
        elif d == 1:
            d = 0
            if 0<=robot_r-1<N:
                if room[robot_r-1][robot_c] == 0:
                    robot_r -= 1
        elif d == 2:
            d = 1
            if 0<=robot_c+1<M:
                if room[robot_r][robot_c+1] == 0:
                    robot_c += 1
        else:
            d = 2
            if 0<=robot_r+1<N:
                if room[robot_r+1][robot_c] == 0:
                    robot_r += 1

print(clean_room)