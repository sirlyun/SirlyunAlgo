'''
    NxN 보드
    배열의 요소들은 해당 지역의 높이 
'''

def bfs(x, y, height):
    queue = []
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        now = queue.pop(0)
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            di = now[0]+dx
            dj = now[1]+dy

            if 0<=di<N and 0<=dj<N:
                if board[di][dj] > height and not visited[di][dj]:
                    visited[di][dj] = True
                    queue.append((di, dj))



N = int(input())
board = []
max_chk = 0
for n in range(N):
    chk = list(map(int, input().split()))
    max_chk = max(max_chk, max(chk))
    board.append(chk)

result = 0
for i in range(max_chk):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] > i and not visited[x][y]:
                bfs(x, y, i)
                cnt += 1

    result = max(result, cnt)

print(result)