'''
    NxN크기의 교실
    학생 수 N**2
    각 학생들은 좋아하는 다른 학생 4명이 있다.
    두 학생 사이의 멘헤튼 거리가 1이면 인접한다고 한다
    > 자리 정하기 규칙
        1. 비어있는 칸중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리 정하기
        2. 1을 만족하는 칸이 여러개면 인접한 칸 중에서 비어있는 칸이 가장 많은 곳으로
        3. 2를 만족하는 칸도 여러개면 행의 번호가 가장 작은 칸으로, 그것도 여러개면 열의 번호가 가장 작은 칸으로
'''

import sys
N = int(sys.stdin.readline())
class_list = [[0]*N for _ in range(N)]
students = [list(map(int, sys.stdin.readline().split())) for _ in range(N**2)]

for i in range(N**2):
    student = students[i]

    chk = []
    for i in range(N):
        for j in range(N):
            if class_list[i][j] == 0:
                love = 0
                blank = 0
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    di, dj = i+dx, j+dy
                    if 0<=di<N and 0<=dj<N:
                        if class_list[di][dj] in student[1:]:
                            love += 1
                        if class_list[di][dj] == 0:
                            blank += 1
                chk.append([love, blank, i, j])
    chk.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    class_list[chk[0][2]][chk[0][3]] = student[0]

result = 0
students.sort()

for i in range(N):
    for j in range(N):
        cnt = 0
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            di, dj = i+dx, j+dy
            if 0<=di<N and 0<=dj<N:
                if class_list[di][dj] in students[class_list[i][j]-1]:
                    cnt += 1
        if cnt != 0:
            result += 10**(cnt-1)

print(result)