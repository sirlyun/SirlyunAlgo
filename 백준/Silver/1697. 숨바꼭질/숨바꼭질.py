def bfs(start):
    queue = []
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.pop(0)
        if now == K:
            return
        if 0<=now-1<=100000:
            if not visited[now-1]:
                visited[now-1] = True
                check[now-1] = check[now]+1
                queue.append(now-1)
        if 0<=now+1<=100000:
            if not visited[now+1]:
                visited[now+1] = True
                check[now+1] = check[now]+1
                queue.append(now+1)
        if 0<=now*2<=100000:
            if not visited[now*2]:
                visited[now*2] = True
                check[now*2] = check[now]+1
                queue.append(now*2)


N, K = map(int, input().split())
check = [1]*100001
visited = [False]*100001
bfs(N)
print(check[K]-1)