'''
    바이러스는 상하좌우 인접한 칸으로 전파가능
    새로 세울 수 있는 벽의 개수는 3개이고 무조건 3개 다 세워야함
    1은 벽, 2는 바이러스
'''

def dfs(cnt):
    global max_cnt, visited
    if cnt == 3:
        for n in range(N):
            for m in range(M):
                if map_list[n][m] == 2:
                    bfs((n, m))
        result = 0
        for k in range(N):
            for l in range(M):
                if not visited[k][l] and map_list[k][l] == 0:
                    result += 1

        if max_cnt < result:
            max_cnt = result
        visited = [[False]*M for _ in range(N)]
        return
        
    for i in range(N):
        for j in range(M):
            if map_list[i][j] == 0:
                map_list[i][j] = 1
                dfs(cnt+1)
                map_list[i][j] = 0

def bfs(start):
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = True
    while queue:
        now = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            di = now[0]+dx
            dj = now[1]+dy
            if 0<=di<N and 0<=dj<M:
                if map_list[di][dj] not in (1, 2) and not visited[di][dj]:
                    visited[di][dj] = True
                    queue.append((di, dj))
                
    return

N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
max_cnt = 0

dfs(0)
print(max_cnt)