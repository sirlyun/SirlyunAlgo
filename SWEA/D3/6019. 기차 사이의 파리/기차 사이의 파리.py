T = int(input())
for t in range(1, T+1):
    D, A, B, F = map(int, input().split())

    time = D / (A+B)
    print(f'#{t}', F*time)