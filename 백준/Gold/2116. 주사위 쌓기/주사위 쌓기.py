'''
    주사위에 1부터 6까지의 숫자가 적혀있음
    아래에서부터 1번 주사위, 2번 주사위... 쌓기
    규칙
        서로 붙어 있는 두 개 주사위에서 아래에 있는 주사위의 윗면에 적힌 숫자는 위에 있는 주사위 아랫면 숫자와 같음
    쌓으면 긴 사각 기둥과 같은 형태가 된다
    사각 기둥의 옆면들 중 어느 한 면의 숫자 합이 최대가 되도록 한다.
    주사위를 상하 고정한 체 옆으로 돌리며 최대가 되도록 만들 수 있다.

    위 아래 짝을 맞춰준다
    주사위의 윗면 아랫면 가능한 경우 모두 탐색?
'''

N = int(input())
dice_list = [list(map(int, input().split())) for _ in range(N)]
dice_dict = {
    0: 5,
    1: 3,
    2: 4,
    5: 0,
    3: 1,
    4: 2
}

max_num = 0
for i in range(6):
    result = []
    tmp_idx = i
    top_idx = dice_dict[tmp_idx]
    chk = []
    for d in range(6):
        if d != tmp_idx and d != top_idx:
            chk.append(dice_list[0][d])
    result.append(chk)
    top = dice_list[0][top_idx]
    for dice in dice_list[1:]:
        tmp_idx = dice.index(top)
        top_idx = dice_dict[tmp_idx]
        top = dice[top_idx]
        c = []
        for k in range(6):
            if k != tmp_idx and k != top_idx:
                c.append(dice[k])
        result.append(c)
    max_chk = 0
    for r in result:
        max_chk += max(r)
    if max_chk > max_num:
        max_num = max_chk

print(max_num)