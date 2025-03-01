"""
    일직선 위에 높이가 다른 N개의 탑이 있고, 각 탑의 꼭대기에 송신기가 있다
    송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사한다
    하나의 탑에서 발사된 레이저는 가장 먼저 만나는 탑에서만 수신 가능

    탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는가
"""

import sys

N = int(sys.stdin.readline())
top_height = list(map(int, sys.stdin.readline().split()))
top_cnt = len(top_height)
check = []
result = [0]*N

check.append(0)
for idx in range(1, top_cnt):
    while check:
        if top_height[check[-1]] > top_height[idx]:
            result[idx] = check[-1]+1
            break
        else:
            check.pop()

    check.append(idx)

print(*result)