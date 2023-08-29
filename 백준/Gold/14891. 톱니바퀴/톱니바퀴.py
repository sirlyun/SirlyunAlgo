'''
    톱니바퀴 4개
        1번 바퀴: s n s n s s s s
        2번 바퀴: n s s s s s n s
        3번 바퀴: s s n n s s s n 
        4번 바퀴: n n n n n n s n

    톱니바퀴를 k번 회전 시킨다.
    톱니바퀴를 회전시키려면 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다.
    톱니바퀴를 회전할 때 옆에있는 톱니바퀴와 서로 맞닿은 톱니의 극이 다르다면 그 톱니바퀴는 반대방향으로 회전한다.
    만약에 극이 같으면 회전 안함
'''

def rotate(num, direct):
    if not visited[num]:
        visited[num] = True
        rotate_list[num] = direct

    if num == 0:
        if wheel[num][2] != wheel[num+1][-2]:
            if not visited[num+1]:
                rotate(num+1, -direct)
    elif num == 3:
        if wheel[num][-2] != wheel[num-1][2]:
            if not visited[num-1]:
                rotate(num-1, -direct)
    else:
        if wheel[num][-2] != wheel[num-1][2]:
            if not visited[num-1]:
                rotate(num-1, -direct)
        if wheel[num][2] != wheel[num+1][-2]:
            if not visited[num+1]:
                rotate(num+1, -direct)
        

def rotate_go(num):
    wheel[num].append(wheel[num].pop(0))

def rotate_back(num):
    wheel[num].insert(0, wheel[num].pop())

wheel = []
for i in range(4):
    chk = []
    for j in input():
        chk.append(j)
    wheel.append(chk)

K = int(input())
for k in range(K):
    visited = [False]*4
    rotate_list = [0, 0, 0, 0]
    rotate_wheel, direct = map(int, input().split())
    rotate(rotate_wheel-1, direct)
    
    for w in range(4):
        if rotate_list[w] == 1:
            rotate_back(w)
        elif rotate_list[w] == -1:
            rotate_go(w)
        else:
            continue

result = 0
for w in range(4):
    if wheel[w][0] == '1':
        result += 2**w

print(result)