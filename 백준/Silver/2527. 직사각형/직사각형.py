'''
    직사각형의 왼쪽 아래 꼭짓점 x, y와 오른쪽 위 꼭짓점 p, q
    겹치는 부분의 특성에 따라 분류
        겹치는 부분이 직사각형인 경우 -> a
        겹치는 부분이 선분인 경우 -> b
        겹치는 부분이 점인 경우 -> c
        없는 경우 -> d
'''

for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if p1 < x2 or q1 < y2 or x1 > p2 or y1 > q2:
        print('d')
    elif (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2) or (x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1):
        print('c')
    elif p1 == x2 or x1 == p2 or y1 == q2 or y2 == q1:
        print('b')
    else:
        print('a')
