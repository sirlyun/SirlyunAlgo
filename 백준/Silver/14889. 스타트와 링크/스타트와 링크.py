'''
    축구를 하기 위해 모인 N명 (짝수)
    N/2로 이루어진 스타트 팀과 링크 팀
    사람에게 번호를 1부터 N까지 배정
    능력치 Sij는 i번 사람과 j번 사람이 같은 팀일 때 팀에 더해지는 능력치
    팀 능력치는 팀에 속한 모든 쌍의 능력치 Sij 합
    Sij와 Sji는 다를 수 있고 팀에 더해지는 능력치는 Sij와 Sji이다
    두 팀의 능력치 차이를 최소화
'''

import sys
N = int(sys.stdin.readline())
power_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False]*N
result = 2147000000

def dfs(depth, idx):
    global result
    if depth == N//2:
        a, b = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    a += power_list[i][j]
                elif not visited[i] and not visited[j]:
                    b += power_list[i][j]
        result = min(result, abs(a-b))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(result)