T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    word_list = []
    for _ in range(N):
        place = list(map(int, input().split()))
        word_list.append((place))

    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if word_list[i][j] == 1:
                cnt += 1
            if word_list[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0

        for j in range(N):
            if word_list[j][i] == 1:
                cnt += 1
            if word_list[j][i] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0

    print(f'#{t} {result}')