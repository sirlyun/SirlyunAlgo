def dfs(day, total):
    global max_result
    if day == N:
        max_result = max(max_result, total)
        return

    if day + day_list[day][0] <= N:
        dfs(day + day_list[day][0], total + day_list[day][1])
    
    dfs(day+1, total)


N = int(input())
day_list = [list(map(int, input().split())) for _ in range(N)]
max_result = 0
dfs(0, 0)
print(max_result)