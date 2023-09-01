def dfs(start, score, cnt):
    global max_score
    if cnt == 4:
        if max_score < score:
            max_score = score
        return
    
    for k in range(4):
        di = start[0]+control_list[k][0]
        dj = start[1]+control_list[k][1]
        if 0<=di<N and 0<=dj<M:
            if not visited[di][dj]:
                visited[di][dj] = True
                dfs((di, dj), score+board[di][dj], cnt+1)
                visited[di][dj] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
control_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
max_score = 0

check = []
for i in range(1<<4):
    chk = []
    for j in range(i):
        if i & (1<<j):
            chk.append(control_list[j])
    if len(chk) == 3:
        check.append(chk)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs((i, j), board[i][j], 1)
        visited[i][j] = False

        score = 0
        for c in check:
            chk_score = board[i][j]
            for dx, dy in c:
                di = i+dx
                dj = j+dy
                if 0<=di<N and 0<=dj<M:
                    chk_score += board[di][dj]
                else:
                    break
            if score < chk_score:
                score = chk_score

        if max_score < score:
            max_score = score

print(max_score)