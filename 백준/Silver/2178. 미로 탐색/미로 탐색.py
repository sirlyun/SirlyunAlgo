def bfs(start):
    queue = []
    queue.append(start)
    while queue:
        now = queue.pop(0)
        if now == (N-1, M-1):
            return
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            di = now[0] + dx
            dj = now[1] + dy
            if 0<=di<N and 0<=dj<M:
                if not visited[di][dj] and miro[di][dj]:
                    visited[di][dj] = True
                    queue.append((di, dj))
                    depth[di][dj] = depth[now[0]][now[1]] + 1


import sys
N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, input())) for _ in range(N)]
depth = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
visited[0][0] = True
bfs((0, 0))
print(depth[N-1][M-1]+1)