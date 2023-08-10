'''
    가로, 세로 길이 주어짐
    2차원 배열 생성 필요
    잘라야 할 점선들이 주어짐
    가장 큰 종이 조각의 넓이를 구해야함
'''

N, M = map(int, input().split())
x_list = [0, N]
y_list = [0, M]
T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    if a == 0:
        y_list.append(b)
    elif a == 1:
        x_list.append(b)

x_list.sort()
y_list.sort()

cnt_x, cnt_y = 0, 0
pre = 0

for x in x_list:
    if x - pre > cnt_x:
        cnt_x = x - pre
    pre = x

pre = 0
for y in y_list:
    if y - pre > cnt_y:
        cnt_y = y - pre
    pre = y

print(cnt_x*cnt_y)