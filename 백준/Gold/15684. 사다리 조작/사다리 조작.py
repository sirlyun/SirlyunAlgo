'''
    사다리 게임은 N개의 세로선과 M개의 가로선으로 되어있다.
    인접한 세로선 사이에는 가로선을 놓을 수 있는데 각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H이다.
    모든 세로선이 같은 위치를 가진다.
    두 가로선이 연속하거나 서로 접하면 안 된다.
    i번 세로선의 결과가 i번이 나오도록 조작
    그를 위해 추가해야하는 가로선의 개수 최솟값
'''

def check():
    for i in range(N):
        tmp = i
        for j in range(H):
            if map_list[j][tmp]:
                tmp += 1
            elif tmp > 0 and map_list[j][tmp - 1]:
                tmp -= 1
        if tmp != i:
            return False
    return True


def makeCross(cnt, x, y):
    global min_cnt

    if min_cnt <= cnt:
        return
    
    if check():
        min_cnt = min(min_cnt, cnt)
        return

    for i in range(x, H):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, N-1):
            if map_list[i][j] == 0:
                map_list[i][j] = 1
                makeCross(cnt+1, i, j+2)
                map_list[i][j] = 0

import sys
input = sys.stdin.readline
N, M, H = map(int, input().split())
cross_list = []
for _ in range(M):
    cross_list.append(list(map(int, input().split())))
map_list = [[0]*(N) for _ in range(H)]
for cross in cross_list:
    map_list[cross[0]-1][cross[1]-1] = 1
min_cnt = 4
makeCross(0, 0, 0)
if min_cnt == 4:
    print(-1)
else:
    print(min_cnt)