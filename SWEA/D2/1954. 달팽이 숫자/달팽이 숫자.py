T = int(input())
for t in range(1, T+1):
    N = int(input())
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    result_list = [[0]*N for i in range(N)]
    row, col = 0, 0
    dist = 0

    for n in range(1, N * N + 1):
        result_list[row][col] = n
        row += dr[dist]
        col += dc[dist]

        if row < 0 or col < 0 or row >= N or col >= N or result_list[row][col] != 0:
            row -= dr[dist]
            col -= dc[dist]
            dist = (dist + 1) % 4

            row += dr[dist]
            col += dc[dist]

    print(f'#{t}')
    for result in result_list:
        for r in result:
            print(r, end=' ')
        print()
