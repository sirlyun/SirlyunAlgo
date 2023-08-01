for t in range(10):
    N = int(input())
    b_list = list(map(int, input().split()))

    chk = 0
    for b in range(2, N-2):
        arMax = 0
        for i in range(b-2,b+3):
            if i != b:
                if arMax < b_list[i]:
                    arMax = b_list[i]
        if b_list[b] > arMax:
            chk += b_list[b] - arMax

    print(f'#{t+1} {chk}')

