'''
    NxN 크기의 공간에 물고기 M마리와 상어 1마리 존재
    한칸에 물고기 최대 1마리 존재 가능
    상어와 물고기 모두 크기가 있다.
    초기 상어의 크기는 2
    상어는 1초에 상하좌우로 인접한 칸으로 1칸 이동
        이동할 때 상어보다 큰 몸집의 물고기가 거주중인 공간으로는 이동 불가
    상어는 자기보다 작은 크기의 물고기 섭취 가능
    상어와 같은 크기의 물고기는 먹을 수는 없지만 이동에 제약은 없음
    상어가 어디로 이동할지 정하는 방법
        더 이상 먹을 수 있는 물고기가 없으면 엄마상어에게 도움 요청
        먹을 수 있는 물고기가 1마리면 그 물고기 먹으러 간다
        먹을 수 있는 물고기가 여러마리면 가장 가까운 물고기 먹으러감
    거리는 상어가 있는 칸에서 물고기 있는 칸으로 이동할 때 지나야하는 칸의 개수 최솟값
    거리가 가까운 물고기가 많으면 가장 위쪽에 있는 물고기, 그것도 여러마리면 가장 왼쪽에 있는 물고기
    상어의 이동에는 1초가 걸린다
    이동과 섭취는 동시에 발생
    섭취하면 해당 칸이 빈칸이됨
    상어가 자기 몸집만큼 물고기 개수를 먹으면 몸집 1증가
    몇초동안 엄마상어 도움 요청안하고 물고기 먹을 수 있는지 체크

    0: 빈 칸
    1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
    9: 아기 상어의 위치
'''



def bfs(shark_idx):
    queue = [shark_idx]
    distance[shark_idx[0]][shark_idx[1]] = 0
    while queue:
        now_idx = queue.pop(0)
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            di = now_idx[0]+dx
            dj = now_idx[1]+dy
            if 0<=di<N and 0<=dj<N:
                if distance[di][dj] == -1 and shark_size >= arr[di][dj]:
                    distance[di][dj] = distance[now_idx[0]][now_idx[1]] + 1
                    queue.append([di, dj])
    



N = int(input())
arr = []
shark_idx = []
# 상어 크기와 위치 저장
# 물고기 크기와 위치 저장

for i in range(N):
    chk = list(map(int, input().split()))
    for j in range(N):
        if chk[j] == 9:
            shark_idx = [i, j]
    arr.append(chk)
arr[shark_idx[0]][shark_idx[1]] = 0


shark_size = 2
eat = 0
result = 0
while True:
    cnt = 0
    distance = [[-1]*N for _ in range(N)]
    bfs(shark_idx)
    for i in range(N):
        for j in range(N):
            if arr[i][j] not in (0, 9) and arr[i][j] < shark_size and distance[i][j] != -1:
                cnt += 1
                break
        else:
            continue
        break
    if cnt == 0:
        break

    
    find = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] not in (0, 9) and shark_size > arr[i][j] and distance[i][j] != -1:
                find.append([distance[i][j], i, j])
    find.sort()

    if find:
        shark_idx = [find[0][1], find[0][2]]
        arr[find[0][1]][find[0][2]] = 0
        eat += 1
        result += distance[find[0][1]][find[0][2]]
    
    if eat == shark_size:
        shark_size += 1
        eat = 0

print(result)