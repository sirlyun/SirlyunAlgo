N = int(input())
map_list = [[0]*101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for n in range(N):
    y, x, d, g = map(int, input().split())
    map_list[x][y] = 1


    chk = [d]
    for i in range(g):
        for j in range(len(chk)-1, -1, -1):
            chk.append((chk[j]+1)%4)

    for i in range(len(chk)):
        x += dx[chk[i]]
        y += dy[chk[i]]
        if 0<=x<101 and 0<=y<101:
            map_list[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if map_list[i][j] == 1 and map_list[i+1][j] == 1 and map_list[i][j+1] == 1 and map_list[i+1][j+1]:
            result += 1

print(result)