'''
    NxM 크기의 사무실
    5개의 CCTV
        1번: 오른쪽 방향 감시
        2번: 좌우 방향 감시
        3번: 상우 방향 감시
        4번: 좌상우 방향 감시
        5번: 상하좌우 방향 감시
    CCTV는 방향에 있는 칸 전체 감시 가능
    CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며
    감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다
    0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호
'''

import copy

def chk(arr, mode, x, y):
    for i in mode:
        di = x
        dj = y

        while True:
            di += dx[i]
            dj += dy[i]

            if di<0 or di>=N or dj<0 or dj>=M:
                break
            if arr[di][dj] == 6:
                break
            elif arr[di][dj] == 0:
                arr[di][dj] = -1


def dfs(depth, arr):
    global result

    if depth == len(cctv_list):
        cnt = 0
        for i in arr:
            cnt += i.count(0)
        result = min(result, cnt)
        return
    
    tmp = copy.deepcopy(arr)
    num, x, y = cctv_list[depth]
    for i in mode[num]:
        chk(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(arr)


mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
office = []
cctv_list = []
for i in range(N):
    data = list(map(int, input().split()))
    office.append(data)
    for j in range(M): 
        if data[j] in (1, 2, 3, 4, 5):
            cctv_list.append([data[j], i, j])

result = 100000000
dfs(0, office)
print(result)