T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    chk_list = sorted(num_list)

    min_chk = N
    max_chk = 0

    for i in range(N):
        if num_list[i] == chk_list[0]:
            if min_chk >= i:
                min_chk = i
        if num_list[i] == chk_list[N-1]:
            if max_chk <= i:
                max_chk = i

    print(f'#{t+1} {abs(min_chk-max_chk)}')