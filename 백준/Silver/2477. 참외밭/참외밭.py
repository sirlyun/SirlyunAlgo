n = int(input())
ground_list = []
max_length = [(0, 0), (0, 0)]

for i in range(6):
    d, w = map(int, input().split())
    if d <= 2:
        d = 0
    else:
        d = 1

    if w > max_length[d][1]:
        max_length[d] = (i, w)
    ground_list.append((d, w))

max_sq = max_length[0][1] * max_length[1][1]
check = [False] * 6
for idx, l in max_length:
    for i in idx, (idx + 1) % 6, idx - 1:
        check[i] = True

min_sq = 1
for i in range(6):
    if not check[i]:
        min_sq *= ground_list[i][1]
print((max_sq - min_sq) * n)