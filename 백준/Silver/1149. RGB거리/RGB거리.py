'''
    집이 N개가 있다
    거리는 선분으로 나타낼 수 있다
    집은 빨초파로 칠한다
    각각의 집을 빨초파로 칠하는 비용이 주어졌을 때 규칙을 만족하면서 모든 집을 칠하는 최소 비용
        1. 1번 집의 색은 2번 집의 색과 다르다
        2. N번 집의 색은 N-1번 집의 색과 다르다
        3. i번 집의 색은 양옆 집 색과 다르다
'''

N = int(input())
home_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    home_list[i][0] += min(home_list[i-1][1], home_list[i-1][2])
    home_list[i][1] += min(home_list[i-1][0], home_list[i-1][2])
    home_list[i][2] += min(home_list[i-1][0], home_list[i-1][1])

print(min(home_list[N-1]))