
def bfs():
    queue = deque()
    for i in range(M):
        for j in range(N):
            if map_list[i][j] == 1:
                queue.append((i, j))
                
    while queue:
        now = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            di = now[0]+dx
            dj = now[1]+dy
            if 0<=di<M and 0<=dj<N:
                if map_list[di][dj] == 0:
                    map_list[di][dj] = map_list[now[0]][now[1]] + 1
                    queue.append((di, dj))
                
    return

from collections import deque

N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(M)]

bfs()
            
result = 0
for i in map_list:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))
print(result-1)