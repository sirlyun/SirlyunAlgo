def dfs(start):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        di = start[0]+dx
        dj = start[1]+dy
        if 0<=di<N and 0<=dj<N:
            if home_map[di][dj] != 0 and not visited[di][dj]:
                home_map[di][dj] = cnt
                visited[di][dj] = True
                dfs((di, dj))
    return


N = int(input())
home_map = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 2
chk_list = []
for i in range(N):
    for j in range(N):
        if home_map[i][j] == 1:
            home_map[i][j] = cnt
            visited[i][j] = True
            chk_list.append(cnt)
            dfs((i, j))
            cnt += 1

cnt_list = []
for c in chk_list:
    n = 0
    for i in range(N):
        for j in range(N):
            if c == home_map[i][j]:
                n += 1
    cnt_list.append(n)

print(len(chk_list))
for c in sorted(cnt_list):
    print(c)