T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    bug_list = []
    for n in range(N):
        bug = list(map(int, input().split()))
        bug_list.append(bug)
    max_kill = 0
    for i in range(N):
        for j in range(N):
            chk = 0
            if i+M <= N and j+M <= N:
                for m in range(M):
                    for k in range(M):
                        chk += bug_list[i+m][j+k]
            if max_kill < chk:
                max_kill = chk
    print(f'#{t} {max_kill}')