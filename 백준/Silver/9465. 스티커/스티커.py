T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*N for _ in range(2)]
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    if N > 1:
        dp[0][1] = dp[1][0]+board[0][1]
        dp[1][1] = dp[0][0]+board[1][1]

        for i in range(2, N):
            dp[0][i] = max(dp[1][i-1]+board[0][i], max(dp[0][i-2], dp[1][i-2])+board[0][i])
            dp[1][i] = max(dp[0][i-1]+board[1][i], max(dp[0][i-2], dp[1][i-2])+board[1][i])
        print(max(dp[0][N-1], dp[1][N-1]))
    else:
        print(max(dp[0][N-1], dp[1][N-1]))
    