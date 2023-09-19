'''
    크기가 NxN인 지도
    지도의 각 칸에는 높이가 적혀있다
    이 지도에서 지나갈 수 있는 길이 몇개 있는지 체크
    길은 한 행 또는 한 열 전부를 의미하고 한쪽 끝에서 다른 쪽 끝까지 가는것
    길이 유효하려면 길에 속한 모든 칸의 높이가 같아야 한다.
    경사로를 놓아서 높이를 맞춰줄 수 있다.
    경사로는 높이가 항상 1이며 길이는 L이다.
    개수는 무제한 이다.
    경사로는 낮은 칸과 높은 칸을 연결하며 아래 조건을 만족해야 한다.
        경사로는 낮은 칸에 놓으며 L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
        낮은 칸과 높은 칸의 차이는 1이여야 한다.
        경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고 L개의 칸이 연속되어야 한다.
    불가능한 경우
        경사로를 놓은 곳에 또 경사로를 놓는 경우
        낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
        낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
        경사로를 놓다가 범위를 벗어나는 경우
'''

def check(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            if abs(arr[i]-arr[i-1]) >= 2:
                return False
            if arr[i] < arr[i-1]:
                for j in range(L):
                    if i+j>=N or arr[i] != arr[i+j] or visited[i+j]:
                        return False
                    if arr[i] == arr[i+j]:
                        visited[i+j] = True
            elif arr[i] > arr[i-1]:
                for j in range(L):
                    if i-j-1<0 or arr[i-1] != arr[i-j-1] or visited[i-j-1]:
                        return False
                    if arr[i-1] == arr[i-j-1]:
                        visited[i-j-1] = True


    return True

N, L = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
# 행 기준 체크
for row in map_list:
    visited = [False]*N
    if check(row):
        cnt += 1

new_map = [[row[i] for row in map_list] for i in range(len(map_list[0]))]
for col in new_map:
    visited = [False]*N
    if check(col):
        cnt += 1

print(cnt)