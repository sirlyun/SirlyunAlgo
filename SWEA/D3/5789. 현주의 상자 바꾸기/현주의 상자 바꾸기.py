T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())
    box_list = [0]*N
    for q in range(Q):
        i = q+1
        L, R = map(int, input().split())
        for idx in range(L-1, R):
            box_list[idx] = i

    print(f'#{t}', *box_list)