'''
    NxN 크기의 땅
    각 칸에는 그 칸에 몇명 사는지
    인접한 나라 사이에는 국경선이 존재
    인구이동 진행 방식(더 이상 인구 이동이 불가능할 때까지 진행)
        국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하면 두나라가 공유하는 국경선을 연다
        국경선 열기 체크가 끝나면 인구 이동 시작(하루 단위로 진행)
            국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면 그 나라를 연합이라고 함
            연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) // (연합을 이루고 있는 칸의 개수)가 된다
            연합을 해체하고, 모든 국경선을 닫는다.
'''

def bfs(x, y):
    queue = []
    union = []
    queue.append((x, y))
    union.append((x, y))
    while queue:
        now = queue.pop(0)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            di = now[0]+dx
            dj = now[1]+dy
            if 0<=di<N and 0<=dj<N:
                if L<=abs(land[di][dj]-land[now[0]][now[1]])<=R and not visited[di][dj]:
                    queue.append((di, dj))
                    if (di, dj) not in union:
                        union.append((di, dj))
                    visited[di][dj] = True
    
    return union
    

N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[False]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                chk = bfs(i, j)
                
                if len(chk) > 1:
                    total = 0
                    flag += 1
                    for c in chk:
                        total += land[c[0]][c[1]]
                    for c in chk:
                        land[c[0]][c[1]] = total // len(chk)
    
    if flag == 0:
        break
    cnt += 1

print(cnt)
