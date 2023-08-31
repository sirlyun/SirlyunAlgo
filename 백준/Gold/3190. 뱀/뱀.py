'''
    게임 규칙
        사과를 먹으면 뱀의 길이가 늘어난다
        뱀이 돌아다니다가 벽 또는 자기 몸에 부딪히면 게임이 종료된다
        게임은 NxN 격자에서 진행되고 몇몇칸에는 사과가 있다
        보드 겉은 벽이다
        초기 뱀의 길이는 1이다
        뱀은 처음에 오른쪽을 향한다
        뱀은 매초마다 이동하고 규칙이 있다
            1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 놓는다
            2. 놓은 칸에 사과가 있으면 그 칸의 사과가 사라지고 꼬리는 움직이지 않는다(길이 늘어난 상태)
            3. 없으면 꼬리가 위치한 칸을 비워준다 -> 전체 몸길이 유지
'''

N = int(input())
K = int(input())
apple_idx = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
control_list = []
time_list = []
for _ in range(L):
    a, b = input().split()
    time_list.append(int(a))
    control_list.append(b)

control = (0, 1)
snake = [(0, 0)]
time = 0
while True:
    if time in time_list:
        chk = control_list[time_list.index(time)]
        if chk == 'L':
            if control == (0, 1):
                control = (-1, 0)
            elif control == (-1, 0):
                control = (0, -1)
            elif control == (0, -1):
                control = (1, 0)
            else:
                control = (0, 1)
        if chk == 'D':
            if control == (0, 1):
                control = (1, 0)
            elif control == (1, 0):
                control = (0, -1)
            elif control == (0, -1):
                control = (-1, 0)
            else:
                control = (0, 1)

    di = snake[-1][0]+control[0]
    dj = snake[-1][1]+control[1]
    if 0<=di<N and 0<=dj<N:
        if (di, dj) not in snake:
            if [di+1, dj+1] in apple_idx:
                apple_idx.pop(apple_idx.index([di+1, dj+1]))
                snake.append((di, dj))
            else:
                snake.append((di, dj))
                tail = snake.pop(0)
        else:
            break
    else:
        break
    time += 1

print(time+1)