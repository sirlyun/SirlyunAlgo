grid = [[0]*100 for _ in range(101)]
for i in range(4):
    xi, yi, xj, yj = map(int, input().split())
    for i in range(xi, xj):
        for j in range(yi, yj):
            grid[i][j] += 1

    # print(grid)
result = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] != 0:
            result += 1
print(result)