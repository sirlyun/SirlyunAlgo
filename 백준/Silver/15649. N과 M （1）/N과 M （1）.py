N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
visited = [False]*N
result = []
def dfs(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            result.append(num_list[i])
            visited[i] = True
            dfs(depth+1)
            result.pop()
            visited[i] = False
dfs(0)