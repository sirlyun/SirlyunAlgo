'''
    NxN의 격자
    각 칸에는 바구니 존재, 바구니에는 저장되어 있는 물의 양이 적힘
    비바라기 기술
        1. (N, 1) (N, 2) (N-1, 1) (N-1, 2)에 비구름이 생김
        2. 구름에 이동 M번 명령 이동방향 (←, ↖, ↑, ↗, →, ↘, ↓, ↙) = (1, 2, 3, 4, 5, 6, 7, 8)
            1. 모든 구름이 di방향으로 si칸 이동
            2. 각 구름에서 비가내려 바구니속 물이 1증가
            3. 구름이 모두 사라짐
            4. 2에서 물이 증가한 칸에 물복사버그 마법
                대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
                이때는 배열 이어서 생각 x
            5. 바구니에 있는 물이 2 이상인 모든 칸에 구름이 생기고 물의 양이 2 줄어든다
                이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니여야함
    M번의 이동이 끝난 후 총 물의 양 출력
''' 

N, M = map(int, input().split())
init_list = [list(map(int, input().split())) for _ in range(N)]
control_dict = {
    1: (0, -1),
    2: (-1, -1),
    3: (-1, 0),
    4: (-1, 1),
    5: (0, 1),
    6: (1, 1),
    7: (1, 0),
    8: (1, -1)
}
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for m in range(M):
    d, s = map(int, input().split())
    control = control_dict[d]
    chk_list = []

    for c in clouds:
        di = (c[0]+control[0]*s) % N
        dj = (c[1]+control[1]*s) % N
        chk_list.append((di, dj))
        init_list[di][dj] += 1
        
    for chk in chk_list:    
        cnt = 0
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            i = chk[0]+dx
            j = chk[1]+dy
            if 0<=i<N and 0<=j<N:
                if init_list[i][j] >= 1:
                    cnt += 1
        init_list[chk[0]][chk[1]] += cnt

    check_list = []
    for i in range(N):
        for j in range(N):
            if init_list[i][j]>=2 and (i, j) not in chk_list:
                check_list.append((i, j))
                init_list[i][j] -= 2    
    clouds = check_list
    

result = 0
for i in range(N):
    for j in range(N):
        result += init_list[i][j]

print(result)