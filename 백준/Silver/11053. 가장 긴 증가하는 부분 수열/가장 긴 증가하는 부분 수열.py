N = int(input())
A_list = list(map(int, input().split()))

dp = [1]*N

for n in range(1, N):
    for i in range(n):
        if A_list[n] > A_list[i]:
            dp[n] = max(dp[n], dp[i]+1)

print(max(dp))