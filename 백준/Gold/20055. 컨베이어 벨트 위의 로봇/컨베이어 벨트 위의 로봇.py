'''
    길이가 n인 컨베이어가 있고, 길이가 2n인 벨트가 이 컨베이어를 감싸고 있다
    벨트는 1~n / 2n~n+1 로 나누어짐
    벨트에서 1번이 있는 위치가 올리는 위치, n번이 있는 위치가 내리는 위치
    로봇이 어떤 칸에 도착하면 그 칸의 내구도가 1 감소한다
    로봇을 옮기는 과정
        1. 벨트가 각칸 위에 있는 로봇과 함께 한칸 회전한다
        2. 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동한다. 이동 불가 시 제자리
            로봇이 이동하기 위해선 앞 칸에 로봇이 없고 내구도가 1이상 남아있어야한다
        3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
        4. 내구도가 0인 칸의 개수가 k개 이상이면 과정 종료, 아니면 1로 돌아가
'''

def rotate():
    durable_list.insert(0, durable_list.pop())
    robot.insert(0, robot.pop())


N, K = map(int, input().split())
durable_list = list(map(int, input().split()))
robot = [0]*N
result = 0

while durable_list.count(0) < K:
    # 단계 체크
    result += 1

    # 벨트와 로봇 한칸 회전
    rotate()
    robot[-1] = 0

    # 로봇 자체 이동 체크
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and durable_list[i+1] >= 1:
            robot[i] = 0
            robot[i+1] = 1
            durable_list[i+1] -= 1
    robot[-1] = 0
    # 로봇 올리기
    if robot[0] == 0 and durable_list[0] >= 1:
        robot[0] = 1
        durable_list[0] -= 1

print(result)