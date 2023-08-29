'''
    크기가 NxN인 도시
    도시의 각 칸은 빈칸, 치킨집, 집 중 하나
    치킨거리란 집과 가장 가까운 치킨집 사이의 거리
    치킨거리는 집을 기준으로 하고 치킨거리가 없는 집은 없다
    도시의 치킨 거리는 모든 치킨거리의 합
    임의의 두 칸 사이의 거리는 맨헤튼거리로 구함
'''

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

home_list = []
chick_list = []
# 집 위치와 치킨집 위치들 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home_list.append([i, j])
        elif city[i][j] == 2:
            chick_list.append([i, j])

# M개의 치킨집 정하는 과정
new_chick = []
n = len(chick_list)
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(chick_list[j])
    if len(subset) == M:
        new_chick.append(subset)

result = 100000
for chick in new_chick:
    check = 0
    for home in home_list:
        now_chick = 100000
        for chk in chick:
            if now_chick > abs(home[0]-chk[0]) + abs(home[1]-chk[1]):
                now_chick = abs(home[0]-chk[0]) + abs(home[1]-chk[1])
        check += now_chick
    if result > check:
        result = check
print(result)