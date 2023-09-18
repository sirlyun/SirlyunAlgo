'''
    마법사 상어가 크기가 NxN인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
    i번 파이어볼의 위치는 ri, ci / 질량은 mi이고 방향은 di, 속력은 si이다.
    마법사 상어가 파이어볼에게 이동을 명령하면 다음과 같은 일이 일어난다.
        1. 모든 파이어볼이 자신의 방향 di로 속력 si칸만큼 이동한다.
            이동하는 중에는 같은 칸에 여러개의 파이어볼이 있을 수 있다.
        2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
            1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
            2. 파이어볼은 4개의 파이어볼로 나누어진다.
            3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
                1. 질량은 (합쳐진 파이어볼 질량의 합)//5
                2. 속력은 (합쳐진 파이어볼 속력의 합)//(합쳐진 파이어볼의 개수)
                3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면 방향은 0, 2, 4, 6이 되고 그렇지 않으면 1, 3, 5, 7이 된다.
                4. 질량이 0인 파이어볼은 소멸된다.

    마법사 상어가 이동을 K번 명령한 후 남아있는 파이어볼 질량의 합은?
'''

N, M, K = map(int, input().split())
map_list = [[[] for _ in range(N)] for _ in range(N)]
fire_ball = []
for _ in range(M):
    R, C, M, S, D = map(int, input().split())
    fire_ball.append([R-1, C-1, M, S, D])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fire_ball:
        r, c, m, s, d = fire_ball.pop(0)
        di = (r + s * dx[d]) % N
        dj = (c + s * dy[d]) % N
        map_list[di][dj].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(map_list[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(map_list[i][j])

                while map_list[i][j]:
                    chk = map_list[i][j].pop(0)
                    sum_m += chk[0]
                    sum_s += chk[1]
                    if chk[2] % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

            
                if cnt_odd == cnt or cnt_even == cnt:
                    d_list = [0, 2, 4, 6]
                else:
                    d_list = [1, 3, 5, 7]

                if sum_m//5:    
                    for new_d in d_list:
                        fire_ball.append([i, j, sum_m//5, sum_s//cnt, new_d])

            if len(map_list[i][j]) == 1:
                fire_ball.append([i, j] + map_list[i][j].pop())

result = 0
for f in fire_ball:
    result += f[2]
print(result)