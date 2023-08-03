T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ball_list = []
    for n in range(N):
        flower = list(map(int, input().split()))
        ball_list.append(flower)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    max_pop = 0
    for i in range(N):
        for j in range(M):
            ball = ball_list[i][j]
            for k in range(4):
                di = i + dr[k]
                dj = j + dc[k]

                if 0 <= di < N and 0 <= dj < M:
                    ball += ball_list[di][dj]
            if max_pop < ball:
                max_pop = ball

    print(f'#{t} {max_pop}')