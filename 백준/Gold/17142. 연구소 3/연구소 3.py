'''
    바이러스는 활성화 상태와 비활성화 상태가 있다
    초기에 모든 바이러스는 비활성화 상태
    활성 상태인 바이러스는 상하좌우로 인접한 모든 칸에 동시에 복제되며 1초 걸린다
    연구소의 바이러스 M개를 활성 상태로 변경
    연구소는 NxN 크기
    활성 바이러스가 비활성 바이러스와 만나면 비활성을 활성으로 바꾼다
    0은 빈칸 1은 벽 2는 바이러스

'''

def bfs(start_comb):
    max_time = 0
    time_list = [[1e9]*N for _ in range(N)]
    
    queue = []
    for i in range(M):
        heapq.heappush(queue, (0, start_comb[i]))
        time_list[start_comb[i][0]][start_comb[i][1]] = 0

    while queue:
        if max_time > min_time:
            return
        time, now = heapq.heappop(queue)
        if time_list[now[0]][now[1]] < time:
            continue

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            di = now[0]+dx
            dj = now[1]+dy
            if 0<=di<N and 0<=dj<N:
                if lab_list[di][dj] != 1:
                    if time_list[di][dj] > time+1:
                        time_list[di][dj] = time+1
                        if lab_list[di][dj] == 0:
                            max_time = max(max_time, time+1)
                        heapq.heappush(queue, (time+1, (di, dj)))


    for i in range(N):
        for j in range(N):
            if lab_list[i][j] == 0:
                if time_list[i][j] == 1e9:
                    return
    
    return max_time

    
    

from itertools import combinations
import heapq

N, M = map(int, input().split())
lab_list = []
virus_list = []
exc = 0
for i in range(N):
    chk = list(map(int, input().split()))
    for j in range(N):
        if chk[j] == 2:
            virus_list.append((i, j))
        if chk[j] == 0:
            exc += 1
    lab_list.append(chk)

min_time = 1e9
check = list(combinations(virus_list, M))
cnt = 0
for chk in check:
    time = bfs(chk)
    if time:
        min_time = min(min_time, time)
    else:
        cnt += 1

if exc == 0:
    print(0)
elif cnt == len(check):
    print(-1)
else:
    print(min_time)