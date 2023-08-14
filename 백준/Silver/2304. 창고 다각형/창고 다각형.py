'''
    N개의 기둥이 일렬로 세워져 있다.
    높이는 각각 다를 수 있다.
    조건
        1. 지붕은 수평 부분과 수직 부분으로 구성되며 모두 연결되어야함
        2. 지붕의 수평 부분은 반드시 어느 기둥 윗면과 닿아야함
        3. 지붕의 수직 부분은 반드시 어느 기둥 옆면과 닿아야함
        4. 지붕의 가장자리는 땅에 닿아야함
        5. 오목하게 들어간 부분이 없어야함
'''

N = int(input())
bar_list = sorted([list(map(int, input().split())) for _ in range(N)])

result = 0
idx = 0
for i in bar_list:
    if result < i[1]:
        result = i[1]
        idx = bar_list.index(i)

height = bar_list[0][1]
for bar in range(idx):
    if height < bar_list[bar+1][1]:
        result += (bar_list[bar+1][0] - bar_list[bar][0]) * height
        height = bar_list[bar+1][1]
    else:
        result += (bar_list[bar+1][0] - bar_list[bar][0]) * height

height = bar_list[-1][1]
for bar in range(N-1, idx, -1):
    if height < bar_list[bar-1][1]:
        result += (bar_list[bar][0] - bar_list[bar-1][0]) * height
        height = bar_list[bar-1][1]
    else:
        result += (bar_list[bar][0] - bar_list[bar-1][0]) * height

print(result)